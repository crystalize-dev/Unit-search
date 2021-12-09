from flask_login import UserMixin

from Project import db, manager


class Message(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #sender = db.Column(db.String(512), nullable=False)
    #room = db.Column(db.String(128), nullable=False)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text):
        self.text = text.strip()


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


class Session(db.Model, UserMixin):
    room = db.Column(db.Integer, primary_key=True)
    user_one = db.Column(db.String(128), nullable=False)
    user_two = db.Column(db.String(128), nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
