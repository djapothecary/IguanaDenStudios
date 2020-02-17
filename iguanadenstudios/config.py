import os
from configparser import ConfigParser
from crypto import crypt

basedir = os.path.abspath(os.path.dirname(__file__))

# build the parser
parser = ConfigParser()
parser.read('dev.ini')

# build the 'crypter'
crypter = crypt.Crypt()
crypt_key = 'MyKey4TestingYnP'

class Config:
    #sql database settings
    SECRET_KEY = crypter.decrypt(parser.get('settings', 'secret_key'), crypt_key)
    DRIVER = crypter.decrypt(parser.get('sqldatabase', 'driver'), crypt_key)
    SERVER = crypter.decrypt(parser.get('sqldatabase', 'server'), crypt_key)
    DATABASE = crypter.decrypt(parser.get('sqldatabase', 'database'), crypt_key)
    UID = crypter.decrypt(parser.get('sqldatabase', 'uid'), crypt_key)
    PWD = crypter.decrypt(parser.get('sqldatabase', 'pwd'), crypt_key)

    #sqlite database settings
    SQLITEDB = crypter.decrypt(parser.get('sqlitedatabase', 'sqlitedb'), crypt_key)

    #mail server settings
    MAIL_SERVER = crypter.decrypt(parser.get('mailsettings', 'mail_server'), crypt_key)
    MAIL_PORT = crypter.decrypt(parser.get('mailsettings', 'mail_port'), crypt_key)
    MAIL_USERNAME = crypter.decrypt(parser.get('mailsettings', 'mail_username'), crypt_key)
    MAIL_PASSWORD = crypter.decrypt(parser.get('mailsettings', 'mail_password'), crypt_key)

    #mail fallback settngs
    MAIL_SERVER_FALLBACK = crypter.decrypt(parser.get('mailfallback', 'mail_server_fallback'), crypt_key)
    MAIL_PORT_FALLBACK = crypter.decrypt(parser.get('mailfallback', 'mail_port_fallback'), crypt_key)
    MAIL_USERNAME_FALLBACK = crypter.decrypt(parser.get('mailfallback', 'mail_username_fallback'), crypt_key)
    MAIL_PASSWORD_FALLBACK = crypter.decrypt(parser.get('mailfallback', 'mail_password_fallback'), crypt_key)

    #mail message settings
    MAIL_SUBJECT_PREFIX = crypter.decrypt(parser.get('mail_message', 'mail_subject_prefix'), crypt_key)
    MAIL_SENDER = crypter.decrypt(parser.get('mail_message', 'mail_sender'), crypt_key)

    #TODO:  add godaddy specific configs

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLITEDB = crypter.decrypt(parser.get('dev', 'sqlitedb'), crypt_key)
    MAIL_SERVER = crypter.decrypt(parser.get('dev', 'mail_server'), crypt_key)
    MAIL_PORT = crypter.decrypt(parser.get('dev', 'mail_port'), crypt_key)
    MAIL_USERNAME = crypter.decrypt(parser.get('dev', 'mail_username'), crypt_key)
    MAIL_PASSWORD = crypter.decrypt(parser.get('dev', 'mail_password'), crypt_key)
    MAIL_SERVER_FALLBACK = crypter.decrypt(parser.get('dev', 'mail_server_fallback'), crypt_key)
    MAIL_PORT_FALLBACK = crypter.decrypt(parser.get('dev', 'mail_port_fallback'), crypt_key)
    MAIL_USERNAME_FALLBACK = crypter.decrypt(parser.get('dev', 'mail_username_fallback'), crypt_key)
    MAIL_PASSWORD_FALLBACK = crypter.decrypt(parser.get('dev', 'mail_password_fallback'), crypt_key)
    MAIL_SUBJECT_PREFIX = crypter.decrypt(parser.get('dev', 'mail_subject_prefix'), crypt_key)
    MAIL_SENDER = crypter.decrypt(parser.get('dev', 'mail_sender'), crypt_key)


class TestingConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLITEDB = crypter.decrypt(parser.get('test', 'sqlitedb'), crypt_key)
    MAIL_SERVER = crypter.decrypt(parser.get('test', 'mail_server'), crypt_key)
    MAIL_PORT = crypter.decrypt(parser.get('test', 'mail_port'), crypt_key)
    MAIL_USERNAME = crypter.decrypt(parser.get('test', 'mail_username'), crypt_key)
    MAIL_PASSWORD = crypter.decrypt(parser.get('test', 'mail_password'), crypt_key)
    MAIL_SERVER_FALLBACK = crypter.decrypt(parser.get('test', 'mail_server_fallback'), crypt_key)
    MAIL_PORT_FALLBACK = crypter.decrypt(parser.get('test', 'mail_port_fallback'), crypt_key)
    MAIL_USERNAME_FALLBACK = crypter.decrypt(parser.get('test', 'mail_username_fallback'), crypt_key)
    MAIL_PASSWORD_FALLBACK = crypter.decrypt(parser.get('test', 'mail_password_fallback'), crypt_key)
    MAIL_SUBJECT_PREFIX = crypter.decrypt(parser.get('test', 'mail_subject_prefix'), crypt_key)
    MAIL_SENDER = crypter.decrypt(parser.get('test', 'mail_sender'), crypt_key)

class ProductionConfig(Config):
    DRIVER = crypter.decrypt(parser.get('prod', 'driver'), crypt_key)
    SERVER = crypter.decrypt(parser.get('prod', 'server'), crypt_key)
    DATABASE = crypter.decrypt(parser.get('prod', 'database'), crypt_key)
    UID = crypter.decrypt(parser.get('prod', 'uid'), crypt_key)
    PWD = crypter.decrypt(parser.get('prod', 'pwd'), crypt_key)
    MAIL_SERVER = crypter.decrypt(parser.get('prod', 'mail_server'), crypt_key)
    MAIL_PORT = crypter.decrypt(parser.get('prod', 'mail_port'), crypt_key)
    MAIL_USERNAME = crypter.decrypt(parser.get('prod', 'mail_username'), crypt_key)
    MAIL_PASSWORD = crypter.decrypt(parser.get('prod', 'mail_password'), crypt_key)
    MAIL_SERVER_FALLBACK = crypter.decrypt(parser.get('prod', 'mail_server_fallback'), crypt_key)
    MAIL_PORT_FALLBACK = crypter.decrypt(parser.get('prod', 'mail_port_fallback'), crypt_key)
    MAIL_USERNAME_FALLBACK = crypter.decrypt(parser.get('prod', 'mail_username_fallback'), crypt_key)
    MAIL_PASSWORD_FALLBACK = crypter.decrypt(parser.get('prod', 'mail_password_fallback'), crypt_key)
    MAIL_SUBJECT_PREFIX = crypter.decrypt(parser.get('prod', 'mail_subject_prefix'), crypt_key)
    MAIL_SENDER = crypter.decrypt(parser.get('prod', 'mail_sender'), crypt_key)

config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}