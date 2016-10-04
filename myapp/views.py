from myapp import app
from flask import render_template, request, redirect, url_for
from database  import Article, User, getAllArticles, getArticleByID,getArticlesByTag, createArticle

@app.route('/')
@app.route('/index')
def home():
	articles = getAllArticles();
	newarticles = sorted(articles, key=lambda x: x.time_published, reverse=True);
	return render_template("index.html", articles=newarticles)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/article/<string:id>')
def showArticleDetail(id):
	article = getArticleByID(id=id);
	return render_template("articleDetail.html", article=article)

@app.route('/tag/<string:tag>')
def showArticleByTag(tag):
	articles = getArticlesByTag(tag);
	return render_template("index.html", articles=articles);

@app.route("/newPost")
def newBlogPost():
	return render_template("newBlogPost.html")

@app.route("/post", methods=['GET', 'POST'])
def postArticle():
	title = request.form.get('inputTitle', '')
	content = request.form.get('inputContent', '')
	tag1 = request.form.get('tag1','')
	tag2 = request.form.get('tag2','')
	tag3 = request.form.get('tag3','')
	tag4 = request.form.get('tag4','')
	tags = [];
	if tag1 != '':
		tags.append(tag1);
	if tag2 != '':
		tags.append(tag2);
	if tag3 != '':
		tags.append(tag3);
	if tag4 != '':
		tags.append(tag4);
	cur_user = User.objects().all()[0];
	newArticle = createArticle(title, content, content, cur_user, tags);
	# print newArticle.id
	return redirect(url_for('home'))
	