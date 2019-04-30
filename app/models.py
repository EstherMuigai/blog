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
    category = db.Column(db.String(255),unique = True,index = True)
    content = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blogpost_pic_path = db.Column(db.String())
    blogger_id = db.Column(db.Integer,db.ForeignKey('bloggers.id'))
    comments = db.relationship('Comment',backref = 'blogcomment',lazy="dynamic")
    
    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts = BlogPost.query.order_by(BlogPost.posted.desc()).all()
        return posts

class Visitor(db.Model):
    __tablename__ = 'visitors'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255))
    content = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'comment',lazy="dynamic")

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blogpost_id = db.Column(db.Integer,db.ForeignKey('blogposts.id'))
    visitor_id = db.Column(db.Integer,db.ForeignKey('visitors.id'))

