from iguanadenstudios import app
from flask import render_template, url_for

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