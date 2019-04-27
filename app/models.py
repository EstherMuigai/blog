from . import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash


class Blogger(db.Model,UserMixin):
    __tablename__ = 'bloggers'

    id = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    username = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    joined = db.Column(db.DateTime,default=datetime.utcnow)
    blogposts = db.relationship('BlogPost',backref = 'blogpost',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_blogger(blogger_id):
        return Blogger.query.get(int(blogger_id))

    def __repr__(self):
        return f'Blogger {self.username}'

class BlogPost(db.Model):
    __tablename__ = 'blogposts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blogpost_pic_path = db.Column(db.String())
    blogger_id = db.Column(db.Integer,db.ForeignKey('bloggers.id'))
    