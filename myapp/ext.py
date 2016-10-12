

import os
from mongoengine import *
from flask.ext.mongoengine import MongoEngine
from myapp import app
from global_ import *

#----------------------------------------
# database
#----------------------------------------
# DB_NAME = 'idledustdb'
# DB_USERNAME = 'jc'
# DB_PASSWORD = '12345'
# DB_HOST_ADDRESS = 'ds033086.mlab.com:33086/idledustdb'

# app.config["MONGODB_DB"] = DB_NAME
# connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
# connect()

db = MongoEngine(app) 
# -----------------------------------------------
# By default, Flask-MongoEngine assumes that the mongod instance 
# is running on localhost on port 27017, 
# and you wish to connect to the database named test.
# -------------------------------------------------

import flask_login

login_manager = flask_login.LoginManager()
login_manager.init_app(app)



