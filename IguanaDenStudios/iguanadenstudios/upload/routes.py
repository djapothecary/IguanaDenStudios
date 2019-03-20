from flask import (Blueprint, render_template, redirect, request,
                    url_for, flash, abort)
from flask_login import login_user, login_required, logout_user
from iguanadenstudios import app, db
from iguanadenstudios.upload.forms import UploadForm
from iguanadenstudios.upload.models.upload import (TracklistName,
                                            TracklistDetails)

upload_blueprint = Blueprint('upload', __name__,
                            template_folder = 'templates/upload')

# @upload_blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out')
#     return redirect(url_for('index'))

@upload_blueprint.route('/upload', methods = ['GET', 'POST'])
@login_required
def upload():
    uploadform = UploadForm.UploadForm()

    if uploadform.validate_on_submit():
        artist_dj_name = uploadform.artist_dj_name.data
        tracklist_mix_name = uploadform.tracklist_mix_name.data

        #   commit the dj and tracklist name to the database
        tracklistname = TracklistName(artist_dj_name, tracklist_mix_name)
        db.session.add(tracklistname)
        db.session.commit()

        for track in uploadform.tracklist_mix_details.data.split('\r\n'):
            track_artist = track.split('-', maxsplit = 1)[0]
            track_title = track.split('-', maxsplit = 1)[1]

            details = TracklistDetails(track_artist.rstrip(), track_title.rstrip())
            db.session.add(details)
            db.session.commit()

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('tracklists.tracklists')

            return redirect(next)

    return render_template('/upload.html', form = uploadform)