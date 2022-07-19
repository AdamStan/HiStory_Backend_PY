from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'his_database_pol',
        'USER': 'hist_user',
        'PASSWORD': 'haslo12345',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}