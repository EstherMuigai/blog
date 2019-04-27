from flask import render_template
from . import general

@general.route('/')
def landingpage():
    return render_template('general/landingpage.html')