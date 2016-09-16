from myapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def home():
	return render_template("index.html")

@app.route('/welcome')
@app.route('/welcome.html')
def welcome():
    return render_template("welcome.html")

@app.route('/about')
@app.route('/about.html')
def about():
	return render_template("about.html")

@app.route('/contact')
@app.route('/contact.html')
def contact():
	return render_template("contact.html")