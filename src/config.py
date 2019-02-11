# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'hhgaghhgsdhdhdd')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://<username>:<password>@localhost/<db:name:blog_api_db>')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    'development': Development,
    'production': Production,
}
