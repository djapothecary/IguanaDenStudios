from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class BookingForm(FlaskForm):
    contact_name = StringField('Name*  ', validators = [DataRequired()])
    contact_phone = StringField('Phone*  ', validators = [DataRequired()])
    company_label = StringField('Company/Label')
    artist_band = StringField('Artist/Band')
    email_address = StringField('Email*  ', validators = [DataRequired(), Email()])
    address_1 = StringField('Address 1*  ', validators = [DataRequired()])
    address_2 = StringField('Address 2')
    address_city = StringField('City*  ', validators = [DataRequired()])
    address_state = StringField('State*  ', validators = [DataRequired()])
    address_postal_code = StringField('Postal Code*  ', validators = [DataRequired()], )
    address_country = StringField('Country*  ', validators = [DataRequired()])
    additional_comments = TextAreaField('Additional Comments')
    submit = SubmitField('Submit')