from flask import Blueprint, render_template, redirect, url_for

mastering_blueprint = Blueprint('mastering', __name__,
                                template_folder = 'templates/mastering')

@mastering_blueprint.route('/mastering')
def mastering():
    return render_template('mastering.html')