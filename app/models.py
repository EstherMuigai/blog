from . import db
from datetime import datetime

class Blogger(db.Model):
    __tablename__ = 'bloggers'

    id = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    joined = db.Column(db.DateTime,default=datetime.utcnow)
    bio = db.Column(db.String(255))

    def __repr__(self):
        return f'Blogger {self.username}'