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
