
import os
from mongoengine import *
from flask.ext.mongoengine import MongoEngine
from myapp import app

#----------------------------------------
# database
#----------------------------------------
# DB_NAME = 'idledustdb'
# DB_USERNAME = 'jc'
# DB_PASSWORD = '12345'
# DB_HOST_ADDRESS = 'ds033086.mlab.com:33086/idledustdb'

# app.config["MONGODB_DB"] = DB_NAME
# connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)

connect()
db = MongoEngine(app)
# -----------------------------------------------
# By default, Flask-MongoEngine assumes that the mongod instance 
# is running on localhost on port 27017, 
# and you wish to connect to the database named test.
# -------------------------------------------------


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

# User.objects.delete()
print User.objects.count()
ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()

print(User.objects.count())
l = User.objects().all()[0]
print l.email
print l.first_name
print l.last_name


	
	

    



