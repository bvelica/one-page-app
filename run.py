'''
- run.py file is used to start the app by gunicorn.
- install gunicorn with 'pip install gunicorn and run 'gunicorn run:app' in shell to start the app.
- .env variables are not loaded now.
'''

from app import create_app
from dotenv import load_dotenv


'''
the path to your .env file (or any other file of environment variables you want to load)
'''
load_dotenv('.env')


app = create_app()
