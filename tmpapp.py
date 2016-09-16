
import os
from flask import Flask, render_template
from mongoengine import *
from flask.ext.mongoengine import MongoEngine

#----------------------------------------
# initialization
#----------------------------------------


app = Flask(__name__)
# app.config["SECRET_KEY"] = '-p<\x130|\x10\xe5U\xa8\x96\xcc)\x8c\xdd\\5g\xe7[L\xa3\x1b\xdc'
app.config.from_pyfile('the-config.cfg')
app.config['MONGODB_DB'] = 'project1'
app.config['MONGODB_HOST'] = '127.0.0.1'
app.config['MONGODB_PORT'] = 12345
app.config['MONGODB_USERNAME'] = 'webapp'
app.config['MONGODB_PASSWORD'] = 'pwd123'
db = MongoEngine(app)


# -----------------------------------------------
# By default, Flask-MongoEngine assumes that the mongod instance 
# is running on localhost on port 27017, 
# and you wish to connect to the database named test.
# -------------------------------------------------


#----------------------------------------
# database
#----------------------------------------
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)





#----------------------------------------
# controllers
#----------------------------------------
@app.route('/')
def home():

	return render_template("index.html")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

#----------------------------------------
# launch
#----------------------------------------

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000));
	host = "127.0.0.1";
	# app.run(host=host, port=port, debug=True);
	db.init_app(app)
	ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
	for user in User.objects:
		print user.email
		print user.first_name
	

    



