from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from configparser import ConfigParser
from crypto import crypt

# Globally accessible libraries
login_manager = LoginManager()
db = SQLAlchemy()

#TODO:  may not need this one because of static and mdb bootstrap files
# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()

def create_app(config_name = ''):
    """Initialize the core app"""
    app = Flask(__name__, instance_relative_config = False)

    #app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['CONFIG_NAME'] = config_name
    app.config['ENV'] = 'development'
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    #SQLITEDB = Config.SQLITEDB
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLITEDB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLITEDB

    app.config.from_object('config.DevelopmentConfig')
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    db = SQLAlchemy(app)
    #Migrate(app, db)

    db.init_app(app)

    # initialize login manager
    login_manager.init_app(app)
    # tell login manager what the HTML view is
    login_manager.login_view = 'sign_in'

    with app.app_context():
        # include the routes
        from iguanadenstudios.about_us.routes import about_us_blueprint
        from iguanadenstudios.audiotools.routes import audiotools_blueprint
        from iguanadenstudios.booking.routes import booking_blueprint
        from iguanadenstudios.tracklists.routes import tracklists_blueprint
        from iguanadenstudios.mastering.routes import mastering_blueprint
        from iguanadenstudios.register.routes import register_blueprint
        from iguanadenstudios.sign_in.routes import sign_in_blueprint
        from iguanadenstudios.upload.routes import upload_blueprint
        from iguanadenstudios.error_pages.handlers import error_pages

        # define the index page
        @app.route('/')
        def index():
            return render_template('index.html')

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
