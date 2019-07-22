import os
from configparser import ConfigParser
from crypto import crypt
# build the 'crypter'
crypter = crypt.Crypt()
crypt_key = 'MyKey4TestingYnP'

# config parameters
SECRET_KEY = crypter.encrypt('1guanaDen5tud0s', crypt_key)
DRIVER = crypter.encrypt('SQL SERVER', crypt_key)
SERVER = crypter.encrypt('184.168.47.10', crypt_key)
DATABASE = crypter.encrypt('IguanaDenStudios', crypt_key)
UID = crypter.encrypt('Apoth', crypt_key)
PWD = crypter.encrypt('$6qul62H', crypt_key)

config = ConfigParser()
#basedir = os.path.abspath(os.path.dirname(__file__))

# config['settings'] = {
#     'debug': 'true',
#     'SECRET_KEY': 'iguanadenstudios'#1guanaDen5tud0s
# }

# config['sqldatabase'] = {
#     'DRIVER': 'SQL SERVER',
#     'SERVER': '184.168.47.10',
#     'DATABASE': 'IguanaDenStudios',
#     'UID': 'Apoth',
#     'PWD': '$6qul62H'
# }

config['settings'] = {
    'debug': 'true',
    'SECRET_KEY': SECRET_KEY
}

config['sqldatabase'] = {
    'DRIVER': DRIVER,
    'SERVER': SERVER,
    'DATABASE': DATABASE,
    'UID': UID,
    'PWD': PWD
}

with open('dev.ini', 'w') as f:
    config.write(f)

# with open(basedir + '\\' + 'dev.ini', 'w') as f:
#     config.write(f)