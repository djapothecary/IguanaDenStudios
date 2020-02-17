import os
from iguanadenstudios import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'dev')

if __name__ == "__main__":
    app.run()