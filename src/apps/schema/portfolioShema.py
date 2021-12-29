from src.apps.models.portfolioModel import Portfolio
from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

class PortfolioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Portfolio
    
    id          = ma.auto_field()
    experience  = ma.auto_field()
    imagePath   = ma.auto_field()
    name        = ma.auto_field()
    twitterUser = ma.auto_field()
    email       = ma.auto_field()
    address     = ma.auto_field()
    phone       = ma.auto_field()
    zipCode     = ma.auto_field()