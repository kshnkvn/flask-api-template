from os import path, getenv

from dotenv import load_dotenv

load_dotenv()


class Config:

    BASE_DIR = path.abspath(path.dirname(__file__))

    SECRET_KEY = getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):

    DEBUG = True
    TESTING = True
    SECRET_KEY = 'secret_key'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
