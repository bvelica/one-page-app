### users page blueprint ###
from flask import Blueprint

blueprint_users = Blueprint('blueprint_users', __name__)

@blueprint_users.route('/')
def users():
    return f'Users blueprint page'
