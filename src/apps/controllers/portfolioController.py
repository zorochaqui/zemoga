from src.apps.models.portfolioModel import Portfolio
from src.config.twitter import twitter
from src.apps.schema.portfolioShema import PortfolioSchema
import logging
import tweepy
import src.config.error as error
from src.config.models_cnf.database import db
from sqlalchemy import exc

class PortfolioController:

    # def allPortfolios(self):
    #     try:
    #         users           = Portfolio.query.all()
    #         user_schema     = PortfolioSchema(many=True)
    #         data            = user_schema.dump(users)
    #         return data
    #     except Exception as why:
    #         print(why)
    #         return error.SERVER_ERROR_500

    def portfolio(self, id):
        #lista un perfil de portafolio
        try:
            users           = Portfolio.query.filter_by(id=id).first()
            user_schema     = PortfolioSchema()
            data            = user_schema.dump(users)
            return data
        except Exception as why:
            print(why)
            return error.SERVER_ERROR_500

    def tweets(self, name, quantity):
        #se lista los tweets, segun el nombre y la cantidad de tweets a traer
        try:
            tweet = {}
            group = []
            api = twitter()
            for tweets in tweepy.Cursor(api.user_timeline, screen_name=name,
                        tweet_mode='extended').items(quantity):
                group.append({"tweet":tweets._json["full_text"]})
            tweet["tweets"] = group
            return tweet
        except Exception as why:
            print(why)
            return error.SERVER_ERROR_500
  
    # def search(self):

    #     api = twitter()
    #     user = api.get_user(screen_name="Tesla")._json
    #     #for tweet in public_tweets:
    #     #    print(tweet.text)
    #     return {"id":2222}


    def updatePortfolio(self, ids, data):
        #actualizar el perfil de portafolio
        try:
            sd=db.session.query(Portfolio).filter(Portfolio.id==ids).update(data)
            db.session.commit()
            return {"success": "se actualizó correctamente"}
        except exc.SQLAlchemyError:
            return error.SERVER_ERROR_500
        except Exception as why:
            print(why)
            return error.SERVER_ERROR_500

