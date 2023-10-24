
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/dbeznet"
    APP_SECRET_KEY = "13df53bac782testb9f908c26b09717314546456"
    POSTGRESQL_CONNECTION = "postgresql://postgres:postgres@localhost/dbeznet"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

PORT = 5000
DEBUG = True
APP_SECRET_KEY = "43df53bac7824657b9f908c26b09717314546456"
# Configuracion de bases de datos
POSTGRESQL_CONNECTION = "postgresql://postgres:postgres@localhost/dbeznet"
SQLALCHEMY_TRACK_NOTIFICATIONS = False
