# this will make the website folder a python package
from flask import Flask
from .views import views
from .auth import auth


def create_app():
    # __name__ represents the name of the file that you run
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hidahslkdwakld dhwkajdhsad'
    # register the blueprint. the url_prefix mean that if you want to access all the
    app.register_blueprint(views, url_prefix='/')
    # urls inside of this blueprint, you must start with the / first. For example: inside of views blueprint we have a route like this
    # hello, then we can only access the page with http://127.0.0.1:5000/hello
    app.register_blueprint(auth, url_prefix='/')
    return app
