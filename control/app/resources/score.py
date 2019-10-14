import falcon

from app.resources import BaseResource

class ScoreResource(BaseResource):
    leaderboard = None

    def __init__(self, leaderboard):
        super(ScoreResource, self).__init__()
        self.leaderboard = leaderboard
        
    def on_get(self, req, resp, leaderboard_id, user_id):
        print(self.leaderboard.columns.keys(), flush=True)
        resp.status = falcon.HTTP_200
        resp.media = {
            "score": 25
        }
