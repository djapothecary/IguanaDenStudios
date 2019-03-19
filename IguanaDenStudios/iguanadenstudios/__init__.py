import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

# TODO: store this in a config file
app.config['SECRET_KEY'] = 'iguanadenstudios'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# initialize login manager
login_manager.init_app(app)
# tell login manage what the HTML view is
login_manager.login_view = 'sign_in'

# register blueprints after database is created
# apparently blueprints/routes can't live in a sub folder...!!!!
# from iguanadenstudios.home.views.routes import home_blueprint
# from iguanadenstudios.about_us.views.routes import about_us_blueprint
# from iguanadenstudios.tracklists.views.routes import tracklists_blueprint
# from iguanadenstudios.mastering.views.routes import mastering_blueprint

from iguanadenstudios.about_us.routes import about_us_blueprint
from iguanadenstudios.tracklists.routes import tracklists_blueprint
from iguanadenstudios.mastering.routes import mastering_blueprint
from iguanadenstudios.register.routes import register_blueprint
from iguanadenstudios.sign_in.routes import sign_in_blueprint
from iguanadenstudios.upload.routes import upload_blueprint
from iguanadenstudios.error_pages.handlers import error_pages

# register blueprints
# using url_prefix allows the changing of how the url displays.  the below example produces:
# /about_us/about_us
# app.register_blueprint(about_us_blueprint, url_prefix = '/about_us')
app.register_blueprint(about_us_blueprint)
app.register_blueprint(tracklists_blueprint)
app.register_blueprint(mastering_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(sign_in_blueprint)
app.register_blueprint(upload_blueprint)
app.register_blueprint(error_pages)