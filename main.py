#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv

from flask import Flask

from src.config.routes.routes import generate_routes
from src.config.database import SQLALCHEMY_DATABASE_URI
from src.config.models_cnf.database import db

load_dotenv()
def create_app():
    
    # Create a flask app.
    app = Flask(__name__)

    #What environment the app is running in. Flask and extensions may enable behaviors based on the environment, such as enabling debug mode. The env attribute maps to this config key. This is set by the FLASK_ENV environment variable and may not behave as expected if set in code.
    #production OR development
    app.config["ENV"] = os.getenv("ENV")

    #A secret key that will be used for securely signing the session cookie and can be used for any other security related needs by extensions or your application. It should be a long random bytes or str. For example, copy the output of this to your config:
    # generate secret key python -c 'import secrets; print(secrets.token_hex())'
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    #Enable testing mode. Exceptions are propagated rather than handled by the the app’s error handlers. Extensions may also change their behavior to facilitate easier testing. You should enable this in your own tests.
    app.config["TESTING"] = os.getenv("TESTING")

    # Set debug true for catching the errors.
    app.config['DEBUG'] = os.getenv("DEBUG")

    #server name
    app.config['SERVER_NAME'] = "{0}:{1}".format(os.getenv("DOMAIN"), os.getenv("PORT"))

    #
    app.config["SESSION_COOKIE_SECURE"] = os.getenv("HTTPS")

    app.config["SESSION_COOKIE_HTTPONLY"] = os.getenv("NOJAVASCRIPT")

    # Set database url.
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True

    # Generate routes.
    generate_routes(app)
    
    # Database initialize with app.
    db.init_app(app)

    # Return app.
    return app

if __name__ == '__main__':
    # Create app.
    app = create_app()

    # Run app. For production use another web server.
    # Set debug and use_reloader parameters as False.
    app.run()