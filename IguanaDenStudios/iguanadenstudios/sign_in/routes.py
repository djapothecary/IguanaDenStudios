from flask import (Blueprint, render_template, redirect,
                    url_for, flash, abort, request)
from flask_login import login_user, login_required, logout_user
from iguanadenstudios import app, db
from iguanadenstudios.register.models.register import User
from iguanadenstudios.sign_in.forms import LoginForm

sign_in_blueprint = Blueprint('sign_in', __name__,
                                template_folder = 'templates/sign_in')

@sign_in_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))

@sign_in_blueprint.route('/sign_in', methods =['GET', 'POST'])
def sign_in():
    form = LoginForm.LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Login Successful!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('index')

            return redirect(next)

    return render_template('sign_in.html', form = form)