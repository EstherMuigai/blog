import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://esthermuingai:honeybee@localhost/myblog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://esthermuingai:honeybee@localhost/myblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}