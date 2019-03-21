from wsgiref.handlers import CGIHandler
from iguanadenstudios import app

CGIHandler().run(app)