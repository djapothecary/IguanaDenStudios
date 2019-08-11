from flask import (Blueprint, render_template, redirect, request,
                    url_for, flash, abort)
from flask_login import login_user, login_required, logout_user
from iguanadenstudios.audiotools.forms import ATConvertListForm
# no model added to database,so not imported (yet)

audiotools_blueprint = Blueprint('audiotools', __name__,
                                template_folder = 'templates/audiotools')

@audiotools_blueprint.route('/convert_list', methods = ['GET', 'POST'])
@login_required
def convert_list():
    convert_list_form = ATConvertListForm.ATConvertListForm()

    if convert_list_form.validate_on_submit():
        splitlist = [link.strip() for link in convert_list_form.convert_upload_list.data.split('\r\n')]

        #   TODO:  this needs to be sent to the 'converter'
        #   to get the track name, then that will send to
        #   the downloads page with the splitlist
        return download(splitlist)
    return render_template('/convert_list.html', form = convert_list_form)

def download(splitlist):
    return render_template('downloads.html',
                            splitlist = splitlist)