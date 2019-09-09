import os
from configparser import ConfigParser
from crypto import crypt
# build the 'crypter'
crypter = crypt.Crypt()
crypt_key = 'MyKey4TestingYnP'
basedir = os.path.abspath(os.path.dirname(__file__))

# config parameters
SECRET_KEY = crypter.encrypt('1guanaDen5tud0s', crypt_key)
DRIVER = crypter.encrypt('SQL SERVER', crypt_key)
SERVER = crypter.encrypt('184.168.47.10', crypt_key)
DATABASE = crypter.encrypt('IguanaDenStudios', crypt_key)
SQLITEDB = crypter.encrypt('sqlite:///' + os.path.join(basedir, 'data.sqlite'), crypt_key)
UID = crypter.encrypt('Apoth', crypt_key)
PWD = crypter.encrypt('$6qul62H', crypt_key)
MAIL_SERVER = crypter.encrypt('smtp.djapothecary.com', crypt_key)
MAIL_PORT = crypter.encrypt('587', crypt_key)
MAIL_USERNAME = crypter.encrypt('heydj', crypt_key)
MAIL_PASSWORD = crypter.encrypt('LewisEnrgC0', crypt_key)
MAIL_SERVER_FALLBACK = crypter.encrypt('smtp.googlemail.com', crypt_key)
MAIL_PORT_FALLBACK = crypter.encrypt('587', crypt_key)
MAIL_USERNAME_FALLBACK = crypter.encrypt('djapothecary@gmail.com', crypt_key)
MAIL_PASSWORD_FALLBACK = crypter.encrypt('TheLewisEnrgC0', crypt_key)
MAIL_SUBJECT_PREFIX = crypter.encrypt('[Iguana Den Studios]', crypt_key)
MAIL_SENDER = crypter.encrypt('Iguana Den Studios <heydj@djapothecary.com>', crypt_key)

#TODO:  add godaddy specific configs

config = ConfigParser()

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

config['sqlitedatabase'] = {
    'SQLITEDB': SQLITEDB
}

config['mailsettings'] = {
    'MAIL_SERVER': MAIL_SERVER,
    'MAIL_PORT': MAIL_PORT,
    'MAIL_USERNAME': MAIL_USERNAME,
    'MAIL_PASSWORD': MAIL_PASSWORD
}

config['mailfallback'] = {
    'MAIL_SERVER_FALLBACK': MAIL_SERVER_FALLBACK,
    'MAIL_PORT_FALLBACK': MAIL_PORT_FALLBACK,
    'MAIL_USERNAME_FALLBACK': MAIL_USERNAME_FALLBACK,
    'MAIL_PASSWORD_FALLBACK': MAIL_PASSWORD_FALLBACK
}

config['mail_message'] = {
    'MAIL_SUBJECT_PREFIX': MAIL_SUBJECT_PREFIX,
    'MAIL_SENDER': MAIL_SENDER
}

config['dev'] = {
    'SQLITEDB': SQLITEDB,
    'MAIL_SERVER': MAIL_SERVER,
    'MAIL_PORT': MAIL_PORT,
    'MAIL_USERNAME': MAIL_USERNAME,
    'MAIL_PASSWORD': MAIL_PASSWORD,
    'MAIL_SERVER_FALLBACK': MAIL_SERVER_FALLBACK,
    'MAIL_PORT_FALLBACK': MAIL_PORT_FALLBACK,
    'MAIL_USERNAME_FALLBACK': MAIL_USERNAME_FALLBACK,
    'MAIL_PASSWORD_FALLBACK': MAIL_PASSWORD_FALLBACK,
    'MAIL_SUBJECT_PREFIX': MAIL_SUBJECT_PREFIX,
    'MAIL_SENDER': MAIL_SENDER
}

config['test'] = {
    'SQLITEDB': SQLITEDB,
    'MAIL_SERVER': MAIL_SERVER,
    'MAIL_PORT': MAIL_PORT,
    'MAIL_USERNAME': MAIL_USERNAME,
    'MAIL_PASSWORD': MAIL_PASSWORD,
    'MAIL_SERVER_FALLBACK': MAIL_SERVER_FALLBACK,
    'MAIL_PORT_FALLBACK': MAIL_PORT_FALLBACK,
    'MAIL_USERNAME_FALLBACK': MAIL_USERNAME_FALLBACK,
    'MAIL_PASSWORD_FALLBACK': MAIL_PASSWORD_FALLBACK,
    'MAIL_SUBJECT_PREFIX': MAIL_SUBJECT_PREFIX,
    'MAIL_SENDER': MAIL_SENDER
}

config['prod'] = {
    'DRIVER': DRIVER,
    'SERVER': SERVER,
    'DATABASE': DATABASE,
    'UID': UID,
    'PWD': PWD,
    'MAIL_SERVER': MAIL_SERVER,
    'MAIL_PORT': MAIL_PORT,
    'MAIL_USERNAME': MAIL_USERNAME,
    'MAIL_PASSWORD': MAIL_PASSWORD,
    'MAIL_SERVER_FALLBACK': MAIL_SERVER_FALLBACK,
    'MAIL_PORT_FALLBACK': MAIL_PORT_FALLBACK,
    'MAIL_USERNAME_FALLBACK': MAIL_USERNAME_FALLBACK,
    'MAIL_PASSWORD_FALLBACK': MAIL_PASSWORD_FALLBACK,
    'MAIL_SUBJECT_PREFIX': MAIL_SUBJECT_PREFIX,
    'MAIL_SENDER': MAIL_SENDER
}

config['default'] = {
    'SQLITEDB': SQLITEDB,
    'MAIL_SERVER': MAIL_SERVER,
    'MAIL_PORT': MAIL_PORT,
    'MAIL_USERNAME': MAIL_USERNAME,
    'MAIL_PASSWORD': MAIL_PASSWORD,
    'MAIL_SERVER_FALLBACK': MAIL_SERVER_FALLBACK,
    'MAIL_PORT_FALLBACK': MAIL_PORT_FALLBACK,
    'MAIL_USERNAME_FALLBACK': MAIL_USERNAME_FALLBACK,
    'MAIL_PASSWORD_FALLBACK': MAIL_PASSWORD_FALLBACK,
    'MAIL_SUBJECT_PREFIX': MAIL_SUBJECT_PREFIX,
    'MAIL_SENDER': MAIL_SENDER
}

with open('dev.ini', 'w') as f:
    config.write(f)
