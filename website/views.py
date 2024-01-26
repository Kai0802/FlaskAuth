# stores all the main views or the URL endpoints for the website
from flask import Blueprint, render_template

# Blueprint means that it has a bunch of urls inside
# Flask associates view functions with blueprints when dispatching requests
# and generating URLs from one endpoint to another
views = Blueprint('views', __name__)


@views.route('/')
def home():
    # the point of this function is that this function will run everytime this url is entered
    return render_template("home.jinja")
