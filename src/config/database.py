#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv
load_dotenv()
motor       = os.getenv("DB_MOTOR")
user        = os.getenv("DB_USER")
password    = os.getenv("DB_PASSWORD")
name        = os.getenv("DB_NAME")
port        = os.getenv("DB_PORT")
host        = os.getenv("DB_HOST")
SQLALCHEMY_DATABASE_URI = ""

if motor == "mysql":
    # Create a database in project and get it's path.
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, name)
