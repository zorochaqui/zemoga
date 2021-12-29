from flask_restful import Resource
from flask import g, request

from src.apps.controllers.portfolioController import PortfolioController
import logging

class Portfolio(Resource):

    def get(self, id):
        portfolioController     = PortfolioController()
        user                    = portfolioController.portfolio(id)
        return user
       
    def put(self, id):
        data                    = request.json
        portfolioController     = PortfolioController()
        user                    = portfolioController.updatePortfolio(id,data)
        return user