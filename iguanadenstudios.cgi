#!/wwwroot/Apoth/.local/bin/python2.7
from wsgiref.handlers import CGIHandler

from sys import path
path.insert(0, '/wwwroot/Apoth/personal/iguanadenstudios')

# activate_this = '/wwwroot/Apoth/personal/iguanadenstudios/venv/bin/activate_this.py'
# execfile(activate_this, dict(__file__ = activate_this))

# from app import app as application
from iguanadenstudios import create_app as application

class ProxyFix(object):
    def __init__(self, application):
    self.application = application

def __call__(self, environ, start_response):
    environ['SERVER_NAME'] = "iguanadenstudios.com"
    environ['SERVER_PORT'] = "80"
    environ['REQUEST_METHOD'] = "GET"
    environ['SCRIPT_NAME'] = ""
    environ['PATH_INFO'] = "/"
    environ['QUERY_STRING'] = ""
    environ['SERVER_PROTOCOL'] = "HTTP/1.1"
    return self.application(environ, start_response)

if __name__ == '__main__':
# This is to test if the cgi script can be executed without any errors. Please remember to test only a URL which is valid.
# application.wsgi_app = ProxyFix(application.wsgi_app)
    CGIHandler().run(application) # Run the application using CGI Handler