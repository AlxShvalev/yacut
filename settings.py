import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = (os.getenv('DATABASE_URI') or
                               'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'SECRET_KEY'
