"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

wsgi_app = app.wsgi_app

# TODO: Add any logging levels and handlers with app.logger
# Logging Level Doc: https://docs.python.org/3/library/logging.html
app.logger.setLevel(logging.WARNING) # add log level from Warning and above

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler) # add stream hanlder to app.logger object

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
