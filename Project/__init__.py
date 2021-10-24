from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '8762348756873246587'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MainDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from Project import Classes, Routes


db.create_all()
