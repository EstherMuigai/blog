from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,login_required,logout_user
from . import auth
from ..models import Blogger
from .forms import RegistrationForm, LoginForm
from .. import db

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        blogger = Blogger(email = form.email.data, firstname = form.firstname.data, lastname=form.lastname.data, username = form.username.data,password = form.password.data)
        db.session.add(blogger)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form)

@auth.route('/login',methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        blogger = Blogger.query.filter_by(username= login_form.username.data).first()
        if blogger is not None and blogger.verify_password(login_form.password.data):
            login_user(blogger,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('general.landingpage'))

        flash('Invalid username or Password')

    return render_template('auth/login.html',login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("blogger.profile"))