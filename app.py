import os
# from iguanadenstudios import app, create_app, db
from iguanadenstudios import create_app, db
from flask import render_template, url_for
from flask_migrate import Migrate

app = create_app('dev')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db = db, User = User, Role = Role)

@app.route('/')
def index():
    return render_template('index.html')

# useful debugging trick
# with app.test_request_context():
#     print(url_for('about_us.about_us'))
#     print(url_for('tracklists.tracklists'))
#     print(url_for('mastering.mastering'))

if __name__ == '__main__':
    app.run(debug = True)