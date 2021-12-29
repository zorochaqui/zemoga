from flask import g
from src.config.models_cnf.database import db
from sqlalchemy.sql.expression import bindparam

#estructura de la base de datos

class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    id          = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    experience  = db.Column(db.String(255), nullable=True)
    imagePath   = db.Column(db.String(255), nullable=True)
    name        = db.Column(db.String(255), nullable=True)
    twitterUser = db.Column(db.String(255), nullable=True)
    email       = db.Column(db.String(255), nullable=True)
    address     = db.Column(db.String(255), nullable=True)
    phone       = db.Column(db.String(255), nullable=True)
    zipCode     = db.Column(db.String(255), nullable=True)


