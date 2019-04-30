from flask import Blueprint

myblog = Blueprint('myblog',__name__)

from . import views