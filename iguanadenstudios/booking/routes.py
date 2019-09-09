from flask import (Blueprint, render_template, redirect,
                    url_for, flash, abort, request)
from flask_login import login_user, login_required, logout_user
from iguanadenstudios import db
from iguanadenstudios.booking.models.booking import Booking
from iguanadenstudios.booking.forms import BookingForm

booking_blueprint = Blueprint('booking', __name__,
                                template_folder = 'templates/booking')

@booking_blueprint.route('/booking', methods = ['GET', 'POST'])
def booking():
    form = BookingForm.BookingForm()

    if form.validate_on_submit():
        booking = Booking(contact_name = form.contact_name.data,
                        contact_phone = form.contact_phone.data,
                        company_label = form.company_label.data,
                        artist_band = form.artist_band.data,
                        email_address = form.email_address.data,
                        address_1 = form.address_1.data,
                        address_2 = form.address_2.data,
                        address_city = form.address_city.data,
                        address_state = form.address_state.data,
                        address_postal_code = form.address_postal_code.data,
                        address_country = form.address_country.data,
                        additional_comments = form.additional_comments.data)

        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('booking.html', form = form)


