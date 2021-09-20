import os

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

root = os.path.dirname(__file__)
app = Flask(__name__)
app.config['SECRET_KEY'] = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://gb_btcminer8:HFF8Q-Wae3RW@mysql93.1gb.ru/gb_btcminer8' # intentionally left the data from the database because it will be deleted soon
db = SQLAlchemy(app)
ma = Marshmallow(app)
