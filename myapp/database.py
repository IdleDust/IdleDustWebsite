#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from mongoengine import *
from flask.ext.mongoengine import MongoEngine
from myapp import app
import datetime
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

class User(Document, flask_login.UserMixin):
    email = StringField(required=True)
    username = StringField(max_length=50)
    password = StringField(max_length=50)


# user_loader callback. This callback is used to reload
# the user object from the user ID stored in the session
@login_manager.user_loader
def user_loader(email):
	print "------user_loader active-------"
	users = User.objects(email=email)
	if users.count == 0:
		return;
	user = User()
	user.id = email
	return user

# # This callback should behave the same as your user_loader callback, 
# # except that it accepts the Flask request instead of a user_id.
# @login_manager.request_loader
# def request_loader(request):
# 	print "----------"
# 	print "request_loader active"
# 	email = request.form.get('email')
# 	users = User.objects(email=email)
# 	if users.count == 0:
# 		return; 
# 	user = User()
# 	user.id = email
# 	user.is_authenticated = request.form['pw'] == users[0].password
# 	return user


def createUser(email, username, password):
	user = User();
	user.email = email.lower();
	user.username = username.lower();
	user.password = password.lower();
	user.save();
	return user;


class Article(Document):
	title = StringField(max_length=200, required=True);
	summary = StringField(max_length=500);
	content = StringField();
	author = ReferenceField(User);
	time_published = DateTimeField(default=datetime.datetime.now);
	tags = ListField(StringField(max_length=50));

def createArticle(title, summary, content, author, tags, time_published=None):
	article = Article();
	article.title = title;
	article.summary = summary;
	article.content = content;
	article.author = author;
	if time_published == None :
		article.time_published = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
	else:
		article.time_published = time_published;
	article.tags = tags;
	article.save();

def getAllArticles():
	return Article.objects().all();

def getArticlesByTag(tag):
	print tag;
	articles = [];
	articles = Article.objects(tags=tag);
	print articles;
	newarticles = sorted(articles, key=lambda x: x.time_published, reverse=True);
	for article in newarticles:
		print article.time_published
	return newarticles;

def getArticleByID(id):
	return Article.objects().get(id=id);




User.objects.delete()
email='ross@gmail.com';
username='Ross';
password='example123';
ross = createUser(email, username, password);


print(User.objects.count())
l = User.objects().all()[0]
print l.email + " " + l.username + " " + l.password
# r = User.objects(email=email)
# print r.count()

Article.objects.delete()
title="Fun with the MongoEngine";
author = ross;
content = "Took a look at MongoEngine today, looks pretty cool. looks pretty cool.";
summary = content;
tags = ["mongoengine", "mongodb"];
article1 = createArticle(title, summary, content, author, tags)

title="How To Design Google Docs";
author = ross;
summary = "System design interviews can be quite open-ended and require a wide range of knowledge.";
content = "To prepare well for such kind of interviews," \
"it’s important to cover different areas instead of focusing on a single topic.\n" \
"We’ve spent a lot of time selecting system design questions to analyze, our main criteria are:"\
"The question is popular and classic. \n"\
"We care about the diversity of questions we select\n"\
"The analysis can be helpful to other interview questions\n\n"\
"This week, we’d like to discuss how to design Google Docs. "\
"You will find it quite different from the analysis of our previous questions.";
tags = ["system design", "google docs", "mongodb"];
article2 = createArticle(title, summary, content, author, tags)

# article1 = Article(title="Fun with the MongoEngine", author=ross)
# article1.content = "Took a look at MongoEngine today, looks pretty cool. looks pretty cool.";
# article1.summary = article1.content;
# article1.tags = ["mongoengine", "mongodb"];
# article1.save();

# article2 = Article(title="System Design Interview Questions", author=ross)
# article2.content = "System design interview questions can be quite open-ended";
# article2.tags = ["system design", "mongodb"];
# article2.save();
	
	

    



