import os

class Config(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    DB_DIR = os.getenv('DB_DIR','database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR,'..', DB_DIR, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER =  os.getenv('UPLOAD_FOLDER', os.path.join(BASE_DIR, 'static/uploads'))
    LOG_DIR = os.path.join(BASE_DIR, '../logs')


class Production(Config):
    pass


class Development(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SESSION_COOKIE_SECURE = False
    DEBUG = True