from flask import Blueprint, render_template, redirect, request, url_for
from iguanadenstudios import db
from iguanadenstudios.upload.models.upload import (TracklistName,
                                            TracklistDetails)

tracklists_blueprint = Blueprint('tracklists', __name__,
                                template_folder = 'templates/tracklists')

@tracklists_blueprint.route('/tracklists')
def tracklists():
    #artist_tracklist_name = TracklistName.query.group_by('artist_dj_name', 'tracklist_name_id').all()
    # MS SQL
    artist_tracklist_name = TracklistName.query.group_by().all()
    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name)

@tracklists_blueprint.route('/<int:tracklist_name_id>')
def load_tracklist(tracklist_name_id):
    # MS SQL
    tracklist_details = TracklistDetails.query.filter_by(tracklist_name_id = tracklist_name_id).all()
    td_list = []

    for item in tracklist_details:
        td_list.append(item)

    # MS SQL
    artist_tracklist_name = TracklistName.query.group_by().all()

    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name,
                            td_list = td_list)