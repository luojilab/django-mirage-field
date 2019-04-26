from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": 'mirage',
        'USER': 'yindongliang',
        'PASSWORD': 'yindongliang',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
