import os
from iguanadenstudios import create_app, db
from flask_migrate import Migrate
from configparser import ConfigParser
from crypto import crypt
# from argparse import ArgumentParser

# parser = ArgumentParser(description = 'Configure what settings to use')

# parser.add_argument("-d",
#                     "--dev",
#                     required = False,
#                     type = str,
#                     dest = 'dev',
#                     metavar = 'dev',
#                     help = 'run the application as a developer')
# parser.add_argument('-t',
#                     '--test',
#                     required = False,
#                     type = str,
#                     dest = 'test',
#                     metavar = 'test',
#                     help = 'run the application as a tester')
# parser.add_argument('-p',
#                     '--prod',
#                     required = False,
#                     type = str,
#                     dest = 'prod',
#                     metavar = 'prod',
#                     help = 'run the application in production')
# args = parser.parse_args()


# if args.dev or args.test is not None:
#     print('running dev configuration')
#     app = create_app('dev')
# elif args.prod is not None:
#     print('running prod configuration')
#     app = create_app('prod')
# else:
#     app = create_app('dev')

# migrate = Migrate(app, db)

app = create_app('dev')
migrate = Migrate(app, db)
#app = create_app()

@app.before_first_request
def create_tables():
    # import pdb; pdb.set_trace()
    # if app.config['ENV'] =='development':
    #     import pdb; pdb.set_trace()
    #     db.create_all()
    # else:
    #     db.create_all()

    # check if database exists
    import sqlite3
    #import pdb; pdb.set_trace()
    #existing_db = db_engine.execute("SHOW DATABASES;")
    conn = sqlite3.connect('data.db')
    try:
        conn.execute("SELECT * FROM Tracklists")
    except sqlite3.OperationalError:
        #db_engine = sqla.create_engine('sqlite:///data.db')
        basedir = os.path.abspath(os.path.dirname(__file__))

        # build the parser
        parser = ConfigParser()
        parser.read('dev.ini')

        # build the 'crypter'
        crypter = crypt.Crypt()
        crypt_key = 'MyKey4TestingYnP'
        #sqlite database settings
        SQLITEDB = crypter.decrypt(parser.get('sqlitedatabase', 'sqlitedb'), crypt_key)
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLITEDB

    db.create_all()

if __name__ == "__main__":
    app.run(debug = True)