import os

class Config(object):
    SECRET_KEY = os.environ.get('AMAZON_CLONE2_SECRET', 'secret_key')

class Prodconfig(Config):
    ENV = 'prod'
    DEBUG = False

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True