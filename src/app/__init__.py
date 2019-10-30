from flask import Flask

app = Flask(__name__)

from . import database
database.init_app()

from app import apis