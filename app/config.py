class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '49740a2c2a37bf0e2b89f7'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ariso:Barbie1991@localhost/watchlist'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True