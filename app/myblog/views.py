from flask import render_template,redirect,url_for,abort,request,flash
from . import myblog
import urllib.request,json
from flask_login import current_user
from ..models import Comment,BlogPost,Visitor
from .forms import CommentForm, DeleteButton, EditButton
from .. import db

@myblog.route('/',methods = ['GET','POST'])
def landingpage():
    blogposts = BlogPost.get_posts()
    return render_template('myblog/landingpage.html',id=id,blogposts=blogposts)

@myblog.route('/<title>/<int:id>',methods = ['GET','POST'])
def article(title,id):
    blogpost = BlogPost.query.get(int(id))
    delete=DeleteButton()
    comments = Comment.get_comments(blogpost.id)
    form = CommentForm()
    with urllib.request.urlopen("http://quotes.stormconsultancy.co.uk/random.json") as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
    if form.validate_on_submit():
        if current_user.is_authenticated:
            new_comment = Comment (content = form.comment.data, blogger_id=blogpost.blogger_id,blogpost_id = blogpost.id,)
            new_comment.save_comment()
        else:
            new_visitor = Visitor(username = form.name.data, email = form.email.data)
            new_visitor.save_visitor()
            new_comment = Comment (content = form.comment.data, visitor_id=new_visitor.id, blogpost_id = blogpost.id)
            new_comment.save_comment()
        return redirect(url_for('myblog.article',id=id,blogpost=blogpost,form=form,title=blogpost.title))
    if delete.validate_on_submit():
        db.session.delete(self)
        db.session.commit()
        return redirect(url_for('myblog.article'))
    return render_template('myblog/blogpost.html',id=id,get_quotes_response=get_quotes_response,blogpost=blogpost,form=form,delete=delete,comments=comments)


