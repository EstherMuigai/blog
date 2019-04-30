from flask import render_template,redirect,url_for,abort,request,flash
from . import myblog
from ..models import Comment,BlogPost
from .forms import CommentForm, DeleteButton, EditButton
from .. import db

@myblog.route('/',methods = ['GET','POST'])
def landingpage():
    blogposts = BlogPost.get_posts()
    return render_template('myblog/landingpage.html',id=id,blogposts=blogposts)

@myblog.route('/<int:id>',methods = ['GET','POST'])
def article(id):
    form = CommentForm()
    blogpost = BlogPost.query.get(int(id))
    return render_template('myblog/blogpost.html',id=id,blogpost=blogpost,form=form)


