from flask_restful import Api
from src.apps.view.tweets import Tweets
from src.apps.view.portfolios import Portfolios
from src.apps.view.portfolio import Portfolio

def generate_routes(app):
    # Create api.
    api = Api(app)

    #api.add_resource(Portfolios, "/api/portfolios", endpoint = 'portfolios')
    api.add_resource(Portfolio, "/api/portfolios/<int:id>", endpoint = 'portfolio')
    api.add_resource(Tweets, "/api/portfolios/name/<name>/tweets/<int:quantity>", endpoint = 'tweets')