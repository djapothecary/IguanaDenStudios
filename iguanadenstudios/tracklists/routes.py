from flask import Blueprint, render_template, redirect, request, url_for, request
from iguanadenstudios import db
from iguanadenstudios.upload.models.upload import (TracklistName,
                                            TracklistDetails)

tracklists_blueprint = Blueprint('tracklists', __name__,
                                template_folder = 'templates/tracklists')

@tracklists_blueprint.route('/tracklists')
def tracklists():
    import pdb; pdb.set_trace()
    # MS SQL
    # artist_tracklist_name = TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).all()
    artist_tracklist_name = clean_artist_tracklist_name()
    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name
                            )

@tracklists_blueprint.route('/tracklists/<string:artist_dj_name>', methods = ['GET'])
def load_tracklist(artist_dj_name = '', tracklist_mix_name = ''):
    import pdb; pdb.set_trace()
    # MS SQL
    tracklist_mix_name = request.args.get('tracklist_mix_name')
    tracklist = request.args.get('tracklist_mix_name')

    artist_tracklist_name = clean_artist_tracklist_name()
    if artist_dj_name is not None and tracklist is not None:
        td_list = TracklistDetails.query.with_entities(TracklistDetails.track_artist, TracklistDetails.track_title).join(TracklistName).filter_by(tracklist_mix_name = tracklist).all()

    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name,
                            td_list = td_list
                            )

def clean_artist_tracklist_name():
    import pdb; pdb.set_trace()

    djs = TracklistName.query.with_entities(TracklistName.artist_dj_name).group_by(TracklistName.artist_dj_name).all()
    cleaned_list = []

    for dj in djs:
        glued = []
        temp_list = []
        trackListNames = (TracklistName.query.with_entities(TracklistName.tracklist_mix_name).filter_by(artist_dj_name = dj[0]).group_by(TracklistName.tracklist_mix_name).all())

        for name in trackListNames:
            temp_list.append(name[0])
        glued = (dj[0], temp_list)
        cleaned_list.append(glued)

    return cleaned_list

