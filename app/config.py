class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False}
    JSON_AS_ASCII = False
    DEBAG = True

