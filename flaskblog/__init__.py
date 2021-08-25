from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='views')  # is a special variable in python that is just the name of the module
app.config['SECRET_KEY'] = '1234567890'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # '///' means the relative path from current directory
db = SQLAlchemy(app)

from flaskblog import routes
