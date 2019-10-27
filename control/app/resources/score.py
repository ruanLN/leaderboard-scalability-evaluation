import falcon

from sqlalchemy.dialects.mysql import insert
from sqlalchemy.sql import select, and_
from app.leaderboard_status import LeaderboardStatus
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
        query = select([self.leaderboard]) \
            .where(and_(self.leaderboard.c.leaderboard_id == leaderboard_id, self.leaderboard.c.user_id == user_id))
        result = self.conn.execute(query)
        if result.rowcount != 1:
            resp.status = falcon.HTTP_400
            resp.media = {
                "error_message": "leaderboard player not found",
            }
        else:
            user = result.fetchone()
            resp.status = falcon.HTTP_200
            resp.media = {
                "score": user["score"]
            }

    def on_post(self, req, resp, leaderboard_id, user_id, score):
        status_query = select([self.leaderboard_control.c.status]) \
            .where(self.leaderboard_control.c.leaderboard_id == leaderboard_id)
        result = self.conn.execute(status_query)
        if result.rowcount != 1:
            resp.status = falcon.HTTP_400
            resp.media = {
                "error_message": "leaderboard status not found",
            }
        else:
            status = LeaderboardStatus(result.fetchone()["status"])
            print("status:" + status.name)
            if status != LeaderboardStatus.STARTED:
                resp.status = falcon.HTTP_400
                resp.media = {
                    "error_message": "leaderboard is not STARTED",
                }
            else:
                create_or_update = insert(self.leaderboard)                              \
                    .values(leaderboard_id=leaderboard_id, user_id=user_id, score=score) \
                    .on_duplicate_key_update(score=self.leaderboard.c.score + score)
                result = self.conn.execute(create_or_update)

                query = select([self.leaderboard]) \
                    .where(and_(self.leaderboard.c.leaderboard_id == leaderboard_id,
                                self.leaderboard.columns.user_id == user_id))
                result = self.conn.execute(query)
                if result.rowcount == 0:
                    resp.status = falcon.HTTP_400
                    resp.media = {
                        "error_message": "leaderboard player not found",
                    }
                elif result.rowcount > 1:
                    resp.status = falcon.HTTP_400
                    resp.media = {
                        "error_message": "multiple leaderboard players found",
                    }
                else:
                    updated = result.fetchone()
                    resp.status = falcon.HTTP_200
                    resp.media = {
                        "leaderboard_id": updated["leaderboard_id"],
                        "user_id": updated["user_id"],
                        "score": updated["score"]
                    }
