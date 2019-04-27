import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
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