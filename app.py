import os

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

root = os.path.dirname(__file__)
app = Flask(__name__)
app.config['SECRET_KEY'] = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = 
db = SQLAlchemy(app)
ma = Marshmallow(app)
