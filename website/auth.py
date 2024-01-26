from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    # the text and user are two variables that being passed from backend
    # to front end
    return render_template("login.html.j2", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Log out<p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html.j2")
