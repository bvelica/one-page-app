### index page blueprint ###
from flask import Blueprint

blueprint_index = Blueprint('blueprint_index', __name__)

@blueprint_index.route('/')
def index():
    return 'Bluprint index page'
