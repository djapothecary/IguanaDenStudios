from flask import Blueprint, render_template, redirect, request, url_for
from iguanadenstudios import db
from iguanadenstudios.upload.models.upload import (TracklistName,
                                            TracklistDetails)

tracklists_blueprint = Blueprint('tracklists', __name__,
                                template_folder = 'templates/tracklists')

@tracklists_blueprint.route('/tracklists')
def tracklists():
    import pdb; pdb.set_trace()
    # MS SQL
    artist_tracklist_name = TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).all()
    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name
                            )

@tracklists_blueprint.route('/tracklists/<string:artist_dj_name>')
def load_tracklist(artist_dj_name = '', tracklist_mix_name = ''):
    import pdb; pdb.set_trace()
    # MS SQL
    artist_tracklist_name = TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).all()
    td_list = TracklistDetails.query.with_entities(TracklistDetails.track_artist, TracklistDetails.track_title).join(TracklistName).filter_by(artist_dj_name = artist_dj_name).all()


    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name,
                            td_list = td_list
                            )