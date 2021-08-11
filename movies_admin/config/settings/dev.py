import os

from dotenv import load_dotenv

from .base import *  # noqa

DEBUG = True

load_dotenv()

dsl = {
    'dbname': os.getenv('dbname'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port': os.getenv('port')
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('dbname'),
        'USER': os.getenv('user'),
        'PASSWORD': os.getenv('password'),
        'HOST': os.getenv('host'),
        'PORT': os.getenv('port'),
        'OPTIONS': {
            'options': '-c search_path=content,public',
        }
    }
}
