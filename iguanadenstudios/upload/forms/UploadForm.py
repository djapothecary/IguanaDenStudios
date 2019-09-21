from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, FieldList, TextAreaField, FormField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class UploadForm(FlaskForm):
    #   TODO:   add checkbox to enable file upload
    artist_dj_name = StringField('Artist/DJ Name:  ', validators = [DataRequired()])
    tracklist_mix_name = StringField('Tracklist/Mix title:  ', validators = [DataRequired()])
    tracklist_genre = StringField('Tracklist Genre(s):  ')
    tracklist_mix_details = TextAreaField('Tracklist/Mix Details:  ', validators = [DataRequired()])
    submit = SubmitField('Submit')

def check_dj_and_mix(self, dj, mix):
    if User.query.filter_by(artist_dj_name = dj.data,
                            tracklist_mix_name = mix.data).form.validate_on_submit():
        raise ValidationError('You have already submitted this mix!')
