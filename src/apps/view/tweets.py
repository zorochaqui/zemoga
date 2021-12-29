from flask_restful import Resource

from src.apps.controllers.portfolioController import PortfolioController
import logging

class Tweets(Resource):
    def get(self, name, quantity):
        portfolioController     = PortfolioController()
        user                    = portfolioController.tweets(name, quantity)
        return user