from app import app

import database

@app.route("/")
def index():
    return "Hello world"

@app.route("/about")
def about():
    return "All about Flask"