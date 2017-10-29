from .base import *

TEMPLATES[0]['OPTIONS']['debug'] = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
INTERNAL_IPS = ('127.0.0.1',)
