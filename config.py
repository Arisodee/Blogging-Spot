import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '49740a2c2a37bf0e2b89f7'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ariso:Barbie1991@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    QUOTE_API_BASE_URL = "http://quotes.stormconsultancy.co.uk/random.json" 

    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE = os.environ.get("DATABASE_URL")
    pass 

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ariso:Barbie1991@localhost/blogs' 
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}