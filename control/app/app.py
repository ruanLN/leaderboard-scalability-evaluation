import falcon
import sqlalchemy as db
from app.resources.score import ScoreResource
from app.resources.leaderboard import LeaderboardResource

engine = db.create_engine('mysql://user:password@db:3306/db')
connection = engine.connect()
metadata = db.MetaData()

leaderboard_control = db.Table('leaderboard_control', metadata, autoload=True, autoload_with=engine)

leaderboards = db.Table('leaderboards', metadata, autoload=True, autoload_with=engine)

application = falcon.API()
# Create our resources
leaderboard_res = LeaderboardResource(leaderboard_control, connection)
scores_res = ScoreResource(leaderboards)

application.add_route('/leaderboard', leaderboard_res)
application.add_route('/leaderboard/{leaderboard_id}/start', leaderboard_res, suffix="start")
application.add_route('/score/{leaderboard_id}/{user_id}', scores_res)