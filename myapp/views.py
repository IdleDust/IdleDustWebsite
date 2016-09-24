from myapp import app
from flask import render_template
from database  import Article, User, getAllArticles, getArticleByID

@app.route('/')
@app.route('/index')
def home():
	articles = getAllArticles();
	return render_template("index.html", articles=articles)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/article/<id>')
def showArticleDetail(id):
	article = getArticleByID(id=id);
	return render_template("articleDetail.html", article=article)