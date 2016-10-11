from myapp import app
from flask import render_template, request, redirect, url_for
from database  import Article, User, getAllArticles, getArticleByID,getArticlesByTag, createArticle
from database import login_manager
import flask_login


@app.route('/')
@app.route('/index')
def home():
	articles = getAllArticles();
	newarticles = sorted(articles, key=lambda x: x.time_published, reverse=True);
	return render_template("index.html", articles=newarticles)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return '''
		<form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='pw' id='pw' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
		'''
	email = request.form.get('email', '');
	users = User.objects(email=email);
	if users.count() > 0:
		print users.count()
		if request.form['pw'] == users[0].password:
			user = User()
			user.id = email;
			flask_login.login_user(user);
			return redirect(url_for('protected'))
		return 'Bad Login'
	return 'User not exists'

@app.route('/protected')
@flask_login.login_required
def protected():
    print 'Logged in as: ' + flask_login.current_user.id
    return redirect(url_for('home'))

# callback for login failures
@login_manager.unauthorized_handler
def unauthorized_handler():
	return render_template('unauthorized.html');
	

@app.route('/logout')
@flask_login.login_required
def logout():
	# print "*****"
	# print flask_login.current_user
	flask_login.logout_user();
	return redirect(url_for('home'))

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
@flask_login.login_required
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
	