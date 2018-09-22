from flask import Blueprint, request, render_template, session, url_for
from werkzeug.utils import redirect

import src.models.users.errors as UserErrors
from src.models.users.user import User

__author__ = "abhishekmadhu"


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        # check if login is valid
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email=email, password=password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))    # The . denotes that the method is in current file
            # else, send the user_email an error that the login is invalid, and redirect to the login page
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/login.html')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # check if login is valid
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email=email, password=password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))    # The . denotes that the method is in current file
            # else, send the user_email an error that the login is invalid, and redirect to the login page
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.html')


@user_blueprint.route('/alerts')
def user_alerts():
    return "This is the alerts page"


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass
