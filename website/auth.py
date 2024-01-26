from flask import Blueprint, flash, render_template, request

auth = Blueprint('auth', __name__)


# when going to the url it will be the get request, and when click on submit it will be the post request
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # the text and user are two variables that being passed from backend
    # to front end
    data = request.form
    print(data)
    return render_template("login.html.j2", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Log out<p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif len(firstName) < 2:
            flash('first name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters long.', category='error')
        else:
            flash("Account created!", category='success')

        print(request.form)
    return render_template("sign_up.html.j2")
