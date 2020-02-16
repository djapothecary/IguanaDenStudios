import os
from iguanadenstudios import create_app, db
from iguanadenstudios.register.models.register import User
from flask import render_template, url_for
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



@app.before_first_request
def create_tables():
    import pdb; pdb.set_trace()
    if app.config['ENV'] =='development':
        import pdb; pdb.set_trace()
        db.create_all()
    else:
        db.create_all()


@app.shell_context_processor
def make_shell_context():
    # return dict(db = db, User = User, Role = Role)
    return dict(db = db, User = User)

@app.route('/')
def index():
    return render_template('index.html')

# useful debugging trick
# with app.test_request_context():
#     print(url_for('about_us.about_us'))
#     print(url_for('tracklists.tracklists'))
#     print(url_for('mastering.mastering'))

if __name__ == '__main__':
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
    app.run(debug = True)