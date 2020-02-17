import os
from iguanadenstudios import create_app, db
from flask_migrate import Migrate
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Configure what settings to use')

parser.add_argument("-d",
                    "--dev",
                    required = False,
                    type = str,
                    dest = 'dev',
                    metavar = 'dev',
                    help = 'run the application as a developer')
parser.add_argument('-t',
                    '--test',
                    required = False,
                    type = str,
                    dest = 'test',
                    metavar = 'test',
                    help = 'run the application as a tester')
parser.add_argument('-p',
                    '--prod',
                    required = False,
                    type = str,
                    dest = 'prod',
                    metavar = 'prod',
                    help = 'run the application in production')
args = parser.parse_args()


if args.dev or args.test is not None:
    print('running dev configuration')
    app = create_app('dev')
elif args.prod is not None:
    print('running prod configuration')
    app = create_app('prod')
else:
    app = create_app('dev')

migrate = Migrate(app, db)
#app = create_app('dev')

@app.before_first_request
def create_tables():
    import pdb; pdb.set_trace()
    if app.config['ENV'] =='development':
        import pdb; pdb.set_trace()
        db.create_all()
    else:
        db.create_all()

# @app.shell_context_processor
# def make_shell_context():
#     # return dict(db = db, User = User, Role = Role)
#     return dict(db = db, User = User)

if __name__ == "__main__":
    app.run(debug = True)