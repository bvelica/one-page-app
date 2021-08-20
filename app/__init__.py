
from flask import Flask 

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return f'SECRET_KEY = { app.config.get("SECRET_KEY") }'

    return app
