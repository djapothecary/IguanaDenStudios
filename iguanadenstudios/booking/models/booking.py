from iguanadenstudios import db, login_manager

class Booking(db.Model):

    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key = True)
    contact_name = db.Column(db.String(128))
    contact_phone = db.Column(db.String(9))
    company_label = db.Column(db.String(128))
    artist_band = db.Column(db.String(128))
    email_address = db.Column(db.String(128))
    address_1 = db.Column(db.String(128))
    address_2 = db.Column(db.String(128))
    address_city = db.Column(db.String(64))
    address_state = db.Column(db.String(64))
    address_postal_code = db.Column(db.String(64))
    address_country = db.Column(db.String(64))
    additional_comments = db.Column(db.String)
    #   TODO:  add options for recording vinyl to digital

    def __init__(self, contact_name, contact_phone, company_label,
                artist_band, email_address, address_1, address_2,
                address_city, address_state, address_postal_code,
                address_country, additional_comments):
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.company_label = company_label
        self.artist_band = artist_band
        self.email_address = email_address
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_city = address_city
        self.address_postal_code = address_postal_code
        self.address_country = address_country
        self.additional_comments = additional_comments
