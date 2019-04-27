from flask import render_template
from flask_login import login_required
from . import blogger

@blogger.route('/profile')
@login_required
def profile():
    return render_template('blogger/profile.html')