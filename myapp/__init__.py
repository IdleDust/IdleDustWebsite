from flask import Flask


app = Flask(__name__)
app.config.from_object("myappconfig")





import myapp.views, myapp.models