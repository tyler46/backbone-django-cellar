from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cellar',
        'USER': 'winegrower',
        'PASSWORD': 'm4k3w1n3!',
        'HOST': '',
        'PORT': '',
    }
}


INSTALLED_APPS += ('debug_toolbar', )

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )


APPEND_SLASH = True
