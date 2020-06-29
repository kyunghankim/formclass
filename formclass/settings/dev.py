from .base import *
from decouple import config

# decouple의 config를 활용해 "SECRET_KEY"를 숨겨야함
SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []