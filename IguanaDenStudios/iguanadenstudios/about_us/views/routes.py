from flask import Blueprint, render_template, redirect, url_for
from iguanadenstudios import db # may not be needed

about_us_blueprint = Blueprint('about_us', __name__,
                                template_folder = 'templates/about_us')

@about_us_blueprint.route('/about_us')
def about_us():
    return render_template('about_us.html')