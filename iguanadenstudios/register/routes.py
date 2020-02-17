from flask import (Blueprint, render_template, redirect,
                    url_for, flash, abort)
from flask_login import login_user, login_required, logout_user
from iguanadenstudios import db
from iguanadenstudios.register.models.register import User
# way to fix 'module' is not callable error
# from iguanadenstudios.register.forms.RegistrationForm import RegistrationForm
from iguanadenstudios.register.forms import RegistrationForm

register_blueprint = Blueprint('register', __name__,
                                template_folder = 'templates/register')

# testing logout in a blueprint
# don't know if this will work
@register_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))

@register_blueprint.route('/register', methods = ['GET', 'POST'])
def register():
    # way to fix 'module' is not callable error
    # form = RegistrationForm()
    form = RegistrationForm.RegistrationForm()

    if form.validate_on_submit():
        import pdb; pdb.set_trace()
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        exists = db.session.query(
                db.session.query(User).filter_by(email = form.email.data)
                .exists()).scalar()
        if not exists:
            db.session.add(user)
            db.session.commit()
            flash('Thank you for registering!')
            return redirect(url_for('tracklists.tracklist'))
        else:
            flash('This email address has already been registered!')
            return redirect(url_for('index'))

    return render_template('register.html', form = form)