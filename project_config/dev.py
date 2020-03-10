from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'example@mail.com'

DEBUG = True

SECRET_KEY = '-vc5w$d3lzz4eb5p@etjdrmms&@@09t$vstbed^-h_+j^su^e'

WSGI_APPLICATION = 'project_config.wsgi.dev.application'