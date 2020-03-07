import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'fds;lkcxklnvi23i432klniohj9)$3'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'library.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
