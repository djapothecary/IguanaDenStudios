from flask import Blueprint, render_template, redirect, request, url_for
from iguanadenstudios import db # may not be needed
from iguanadenstudios.upload.models.upload import (TracklistName,
                                            TracklistDetails)

tracklists_blueprint = Blueprint('tracklists', __name__,
                                template_folder = 'templates/tracklists')

@tracklists_blueprint.route('/tracklists')
def tracklists():
    artist_tracklist_name = TracklistName.query.all()
    # artist_tracklist_name = TracklistName.query.join(TracklistDetails).group_by(TracklistDetails.artist_dj_name).all()
    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name)

# @tracklists_blueprint.route('/load_tracklist', methods = ['GET', 'POST'])
# def load_tracklist():
#     #id = form.id.data
#     id = request.form['id']
#     tracklist_to_load = TracklistDetails.query.get(id)

#     return render_template('tracklists.html',
#                             tracklist_to_load = tracklist_to_load)

@tracklists_blueprint.route('/<string:artist_dj_name>')
def load_tracklist(artist_dj_name):
    # tracklist_details = [TracklistDetails.query.get(tracklist_name_id)]
    tracklist_details = [TracklistDetails.query.get(artist_dj_name)]
    # tracklist_details = TracklistDetails.query.join(TracklistName).all()
    td_list = []

    for item in tracklist_details:
        td_list.append(item)

    #tracklist_details = TracklistDetails.query(TracklistDetails).filter_by(id = tracklist_details_id).first()

    artist_tracklist_name = TracklistName.query.all()


    return render_template('tracklists.html',
                            # track_artist = tracklist_details.track_artist,
                            # track_title = tracklist_details.track_title,
                            artist_tracklist_name = artist_tracklist_name,
                            td_list = td_list)