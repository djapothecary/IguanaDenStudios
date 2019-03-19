from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email:  ', validators = [DataRequired(), Email()])
    username = StringField('Username:  ', validators = [DataRequired()])
    password = PasswordField('Password:  ', validators = [DataRequired(), EqualTo('pass_confirm', message = 'Passwords must match')])
    pass_confirm = PasswordField('Confirm Password:  ', validators = [DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).form.validate_on_submit():
            raise ValidationError('Your email has already been registered!')

    def check_username(self, field):
        if User.query.filter_by(username = field.data).form.validate_on_submit():
            raise ValidationError('Your username is already in use!')