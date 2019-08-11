import os
import urllib
from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from iguanadenstudios.config import Config
from configparser import ConfigParser
from crypto import crypt

login_manager = LoginManager()
#TODO:  may not need this one because of static and mdb bootstrap files
# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)

    # build the parser
    parser = ConfigParser()
    parser.read('dev.ini')

    # build the 'crypter'
    crypter = crypt.Crypt()
    crypt_key = 'MyKey4TestingYnP'
    SECRET_KEY = Config.SECRET_KEY

    #load the appropriate configuration
    if config_name == 'dev' or 'test':
        SQLITEDB = Config.SQLITEDB
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLITEDB
        app.config['SECRET_KEY'] = SECRET_KEY
    elif config_name == 'prod':
        DRIVER = Config.DRIVER
        SERVER = Config.SERVER
        DATABASE = Config.DATABASE
        UID = Config.UID
        PWD = Config.PWD
        params = urllib.parse.quote_plus('DRIVER={'+ DRIVER +'};SERVER='+ SERVER +';DATABASE=' + DATABASE +';UID=' + UID +';PWD='+ PWD +';')
        app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = SECRET_KEY
    else:
        SQLITEDB = Config.SQLITEDB
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLITEDB
        app.config['SECRET_KEY'] = SECRET_KEY

    import pdb; pdb.set_trace()
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    # bootstrap.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)

    db = SQLAlchemy(app)
    #Migrate(app, db)

    db.init_app(app)

    # initialize login manager
    login_manager.init_app(app)
    # tell login manager what the HTML view is
    login_manager.login_view = 'sign_in'

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

    return app