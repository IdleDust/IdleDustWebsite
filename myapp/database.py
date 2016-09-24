
import os
from mongoengine import *
from flask.ext.mongoengine import MongoEngine
from myapp import app
import datetime

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
    username = StringField(max_length=50)
    password = StringField(max_length=50)

class Article(Document):
	title = StringField(max_length=200, required=True)
	content = StringField()
	author = ReferenceField(User)
	date_published = DateTimeField(default=datetime.datetime.now)
	tags = ListField(StringField(max_length=50))


def getArticlesByTags(tags):
	articles = []
	for tag in tags:
		articles += Article.objects(tags=tag);
	return articles;
			

def getAllArticles():
	return Article.objects().all();

def getArticleByID(id):
	return Article.objects().get(id=id);

User.objects.delete()
print User.objects.count()
ross = User(email='ross@example.com', username='Ross', password='exam123').save()
print ross.id

print(User.objects.count())
l = User.objects().all()[0]
print l.email
print l.username
print l.password

article1 = Article(title="Fun with the MongoEngine", author=ross)
article1.content = "Took a look at MongoEngine today, looks pretty cool.";
article1.tags = ["mongoengine", "mongodb"];
article1.save();

article2 = Article(title="System Design Interview Questions", author=ross)
article2.content = "System design interview questions can be quite open-ended";
article2.tags = ["system design", "mongodb"];
article2.save();

	
	

    



