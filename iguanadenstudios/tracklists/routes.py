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
    # artist_tracklist_name = TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).all()
    artist_tracklist_name = clean_artist_tracklist_name()
    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name
                            )

@tracklists_blueprint.route('/tracklists/<string:artist_dj_name>')
def load_tracklist(artist_dj_name = '', tracklist_mix_name = ''):
    import pdb; pdb.set_trace()
    # MS SQL
    # artist_tracklist_name = TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).all()

    artist_tracklist_name = clean_artist_tracklist_name()
    td_list = TracklistDetails.query.with_entities(TracklistDetails.track_artist, TracklistDetails.track_title).join(TracklistName).filter_by(artist_dj_name = artist_dj_name).all()


    return render_template('tracklists.html',
                            artist_tracklist_name = artist_tracklist_name,
                            td_list = td_list
                            )

def clean_artist_tracklist_name():
    import pdb; pdb.set_trace()

    djs = TracklistName.query.with_entities(TracklistName.artist_dj_name).group_by(TracklistName.artist_dj_name).all()

    cleaned_list = []
    #temp_list = []
    tracklists = []
    for dj in djs:
        glued = []
        tracklists = (TracklistName.query.with_entities(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).filter_by(artist_dj_name = dj[0]).group_by(TracklistName.artist_dj_name, TracklistName.tracklist_mix_name).all())
        # tracklists = (TracklistName.query.with_entities(TracklistName.tracklist_mix_name).filter_by(artist_dj_name = dj[0]).group_by(TracklistName.tracklist_mix_name).all())
        # tracklists.remove(dj)
        # test = (t for t in tracklists.remove(dj[0]) if tracklists.count(dj[0]) > 1)
        for tracklist in tracklists:
            # temp_list.append(tracklist[0])
            temp_list = {}
            if dj[0] not in glued[0]:
                temp_list = tracklist
                glued.append(temp_list)
            else:
                temp_list = tracklist[1]
                glued.append(temp_list)
        # glued = (dj[0], temp_list)
        cleaned_list.append(glued)
        # cleaned_list.append(temp_list)


    return cleaned_list

