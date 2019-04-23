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
    # artist_tracklist_name = TracklistName.query.group_by().all()
    artist_tracklist_name = TracklistName.query.with_entities(TracklistName.artist_dj_name).group_by(TracklistName.artist_dj_name).all()
    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name#,
                            #djs_tracklists = tracklist_name_list
                            )

# @tracklists_blueprint.route('/tracklists')
# def getDJsLists():
#     tracklists_set = TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).all()
#     tracklist_name_list = []

#     for tracklists in tracklists_set:
#         tracklist_name_list.append(tracklists.tracklist_mix_name)

@tracklists_blueprint.route('/<string:artist_dj_name>')
def load_tracklist(artist_dj_name):
    # MS SQL
    tracklist_details = TracklistDetails.query.filter_by(artist_dj_name = artist_dj_name).all()
    td_list = []

    for item in tracklist_details:
        td_list.append(item)

    tracklists_set = TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name, TracklistName.id).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name, TracklistName.id).all()
    tracklist_name_list = ['tracklist_mix_name', id]

    for tracklists in tracklists_set:
        tracklist_name_list.append(tracklists.tracklist_mix_name)
        tracklist_name_list.append(tracklists.id)

    # MS SQL
    # artist_tracklist_name = TracklistName.query.group_by().all()
    artist_tracklist_name = TracklistName.query.with_entities(TracklistName.artist_dj_name).group_by(TracklistName.artist_dj_name).all()

    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name,
                            #djs_tracklists = tracklist_name_list,
                            td_list = td_list)