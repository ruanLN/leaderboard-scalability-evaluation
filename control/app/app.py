import falcon
import sqlalchemy as db
import time
from app.resources.score import ScoreResource
from app.resources.leaderboard import LeaderboardResource

while True:
    try:
        engine = db.create_engine('mysql://user:password@db:3306/db', echo=True)
        connection = engine.connect()
        metadata = db.MetaData()
        break
    except:
        print("sleeping waiting for database be ready")
        time.sleep(5)

leaderboard_control = db.Table('leaderboard_control', metadata, autoload=True, autoload_with=engine)

leaderboards = db.Table('leaderboards', metadata, autoload=True, autoload_with=engine)

application = falcon.API()
# Create our resources
leaderboard_res = LeaderboardResource(leaderboard_control, connection)
scores_res = ScoreResource(leaderboards, leaderboard_control, connection)

application.add_route('/leaderboard', leaderboard_res)
application.add_route('/leaderboard/{leaderboard_id}', leaderboard_res)
application.add_route('/leaderboard/{leaderboard_id}/start', leaderboard_res, suffix="start")
application.add_route('/leaderboard/{leaderboard_id}/stop', leaderboard_res, suffix="stop")
#application.add_route('/score/{leaderboard_id}/{min_pos}/{size}', scores_res, suffix="view")
#application.add_route('/score/{leaderboard_id}/{user_id}', scores_res)
application.add_route('/score/{leaderboard_id}/{user_id}/{score}', scores_res)