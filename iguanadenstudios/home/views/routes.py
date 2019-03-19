from flask import Blueprint, render_template, redirect, url_for
from iguanadenstudios import db # may not be needed

home_blueprint = Blueprint('home', __name__,
                            template_folder = 'templates/home')

@home_blueprint.route('/index')
def index():
    return render_template('index.html')