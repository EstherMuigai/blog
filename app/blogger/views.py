from flask import render_template
from . import blogger
@blogger.route('/')
def index():
    return render_template('blogger/profile.html')