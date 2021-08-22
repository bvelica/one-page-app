
from flask import Flask 

### Import blueprints ###
from .blueprint_index.index import blueprint_index
from .blueprint_users.users import blueprint_users
### End imports ###

def create_app():
    app = Flask(__name__)

    ### Register blueprints ###
    app.register_blueprint(blueprint_index)
    app.register_blueprint(blueprint_users, url_prefix='/users')
    ### End ###

    return app
