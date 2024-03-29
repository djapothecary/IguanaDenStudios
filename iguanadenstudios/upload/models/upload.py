from iguanadenstudios import db
from datetime import datetime

class TracklistName(db.Model):

    __tablename__ = 'tracklist_names'

    id = db.Column(db.Integer, primary_key = True)
    artist_dj_name = db.Column(db.String)
    tracklist_mix_name = db.Column(db.String)
    tracklist_genre = db.Column(db.String)
    upload_date = db.Column(db.DateTime, default = datetime.utcnow)
    # backrefs need to be unique
    tracklist_id = db.relationship('TracklistDetails', backref = 'artist_dj_id', lazy = True)
    dj_name = db.relationship('TracklistDetails', backref = 'artist_dj_name', lazy = True)
    mix_name = db.relationship('TracklistDetails', backref = 'tracklist_mix_name', lazy = True)

    def __init__ (self, artist_dj_name, tracklist_mix_name):
        self.artist_dj_name = artist_dj_name
        self.tracklist_mix_name = tracklist_mix_name

class TracklistDetails(db.Model):

    __tablename__ = 'tracklist_details'

    #create relationship
    tracklist_name = db.relationship(TracklistName)

    id = db.Column(db.Integer, primary_key = True)
    track_artist = db.Column(db.String)
    track_title = db.Column(db.String)
    tracklist_name_id = db.Column(db.Integer, db.ForeignKey('tracklist_names.id'))

    def __init__ (self, track_artist, track_title, tracklist_name_id):
        self.track_artist = track_artist
        self.track_title = track_title
        self.tracklist_name_id = tracklist_name_id