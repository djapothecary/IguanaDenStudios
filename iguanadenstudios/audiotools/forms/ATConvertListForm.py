from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, FieldList, TextAreaField, FormField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class ATConvertListForm(FlaskForm):
    convert_upload_list = TextAreaField('List to convert:  ',
                            validators = [DataRequired()],
                            description = "Paste the list to convert here...")
    submit = SubmitField('Submit')