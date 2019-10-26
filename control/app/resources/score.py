import falcon

from sqlalchemy.dialects.mysql import insert
from sqlalchemy.sql import select, and_
from app.resources import BaseResource

class ScoreResource(BaseResource):
    leaderboard = None
    leaderboard_control = None
    conn = None

    def __init__(self, leaderboard, leaderboard_control, conn):
        super(ScoreResource, self).__init__()
        self.leaderboard = leaderboard
        self.leaderboard_control = leaderboard_control
        self.conn = conn
        
    def on_get(self, req, resp, leaderboard_id, user_id):
        
        resp.status = falcon.HTTP_200
        resp.media = {
            "score": 25
        }

    def on_post(self, req, resp, leaderboard_id, user_id, score):
        create_or_update = insert(self.leaderboard).values(leaderboard_id = leaderboard_id, user_id = user_id, score = score).on_duplicate_key_update(score=self.leaderboard.columns.score + score)
        result = self.conn.execute(create_or_update)

        query = select([self.leaderboard]).where(and_(self.leaderboard.columns.leaderboard_id == leaderboard_id,  self.leaderboard.columns.user_id == user_id))
        result = self.conn.execute(query)
        if result.rowcount == 0:
            resp.status=falcon.HTTP_400
            resp.media={
                "error_message": "leaderboard player not found",
            }
        elif result.rowcount > 1:
            resp.status=falcon.HTTP_400
            resp.media={
                "error_message": "multiple leaderboard players found",
            }
        else:
            for updated in result:
                print(updated)
                resp.status=falcon.HTTP_200
                resp.media={
                    "leaderboard_id": updated["leaderboard_id"],
                    "user_id": updated["user_id"],
                    "score": updated["score"]
                }
                print(resp)
