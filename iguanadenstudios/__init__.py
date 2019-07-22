import os
import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from configparser import ConfigParser
from crypto import crypt

login_manager = LoginManager()

app = Flask(__name__)

# build the parser
parser = ConfigParser()
parser.read('dev.ini')

# build the 'crypter'
crypter = crypt.Crypt()
crypt_key = 'MyKey4TestingYnP'

SECRET_KEY = crypter.decrypt(parser.get('settings', 'secret_key'), crypt_key)
DRIVER = crypter.decrypt(parser.get('sqldatabase', 'driver'), crypt_key)
SERVER = crypter.decrypt(parser.get('sqldatabase', 'server'), crypt_key)
DATABASE = crypter.decrypt(parser.get('sqldatabase', 'database'), crypt_key)
UID = crypter.decrypt(parser.get('sqldatabase', 'uid'), crypt_key)
PWD = crypter.decrypt(parser.get('sqldatabase', 'pwd'), crypt_key)
app.config['SECRET_KEY'] = SECRET_KEY

basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#   using MS SQL Server
params = urllib.parse.quote_plus('DRIVER={'+ DRIVER +'};SERVER='+ SERVER +';DATABASE=' + DATABASE +';UID=' + UID +';PWD='+ PWD +';')
# params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=184.168.47.10;DATABASE=IguanaDenStudios;UID=Apoth;PWD=$6qul62H;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
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
from iguanadenstudios.audiotools.routes import audiotools_blueprint
from iguanadenstudios.booking.routes import booking_blueprint
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
app.register_blueprint(audiotools_blueprint)
app.register_blueprint(booking_blueprint)
app.register_blueprint(tracklists_blueprint)
app.register_blueprint(mastering_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(sign_in_blueprint)
app.register_blueprint(upload_blueprint)
app.register_blueprint(error_pages)