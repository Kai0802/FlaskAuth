# this will make the website folder a python package
from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy

# this is the new database, we initilize it like the line below
db = SQLAlchemy()
# this is our database's name
DB_NAME = "database.db"


def create_app():
    # __name__ represents the name of the file that you run
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hidahslkdwakld dhwkajdhsad'
    # we a file to store all the information, therefore, we need to register it
    # this is saying that my database is stored in the website folder. We're just telling flask where this is located.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # this is just connecting the app with the database
    # register the blueprint. the url_prefix mean that if you want to access all the
    app.register_blueprint(views, url_prefix='/')
    # urls inside of this blueprint, you must start with the / first. For example: inside of views blueprint we have a route like this
    # hello, then we can only access the page with http://127.0.0.1:5000/hello
    app.register_blueprint(auth, url_prefix='/')
    return app
