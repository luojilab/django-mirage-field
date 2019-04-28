from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "NAME": 'mirage',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
