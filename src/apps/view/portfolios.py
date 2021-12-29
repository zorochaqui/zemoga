from flask_restful import Resource
import src.config.error as error
from src.apps.controllers.portfolioController import PortfolioController
import logging

class Portfolios(Resource):
    @staticmethod
    def get():
        try:
            userController  = PortfolioController()
            allusers        = userController.allUsers()
            return allusers
        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("Error al traer los usuarios " + str(why))

            # Return invalid input error.
            return error.SERVER_ERROR_500