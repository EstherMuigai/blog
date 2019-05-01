import markdown2  
from flask import render_template,redirect,url_for,abort,request,flash
from flask_login import login_required,current_user
from .forms import NewPostForm,DeleteButton,EditButton
from ..email import mail_message
from . import blogger
from .. import db,photos
from ..models import BlogPost,Blogger,Visitor

@blogger.route('/profile')
@login_required
def profile():
    bloggers = Blogger.get_bloggers()
    return render_template('blogger/profile.html',bloggers=bloggers)

@blogger.route('/newpost', methods = ['GET','POST'])
@login_required
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_post = BlogPost(title=form.title.data,content=form.content.data,blogger_id=current_user.id)
        new_post.save_post()
        #visitors = Visitor.query.all()
        #for visitor in visitors:
            #if visitor.email:
               #mail_message("New post on the site!","email/welcome_user",visitor.email,visitor=visitor)
        return redirect(url_for('blogger.blogpost',id = new_post.id ))

    return render_template('blogger/new_post.html',newpost_form=form)

@blogger.route('/blogpost/<int:id>', methods = ['GET','POST'])
def blogpost(id):
    delete = DeleteButton()
    edit = EditButton()
    blogpost=BlogPost.query.get(id)
    if blogpost is None:
        abort(404)
    elif delete.validate_on_submit():
        blogpost.delete_post()
        return redirect(url_for('blogger.new_post'))

    format_post = markdown2.markdown(blogpost.content,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('blogger/blogpost.html', blogpost = blogpost,format_post = format_post,delete = delete, edit = edit)

@blogger.route('/edit/<int:id>', methods = ['GET','POST'])
@login_required
def edit_post(id):
    blogpost=BlogPost.query.get(id)
    form = NewPostForm(formdata=request.form, obj=blogpost)
    if request.method == 'POST' and form.validate_on_submit():
        flash('Post updated successfully!')
        post = BlogPost.query.filter_by(id=id).update({"title": form.title.data,"content": form.content.data})
        db.session.commit()
        return redirect(url_for('blogger.blogpost',id = blogpost.id ))

    return render_template('blogger/edit_post.html',editpost_form = form)
    
@blogger.route('/blogger/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    blogger = Blogger.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        blogger.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('blogger.profile',uname=uname))