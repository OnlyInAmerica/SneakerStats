__author__ = 'davidbrodsky'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blestat',
        'USER': 'davidbrodsky',
        'PASSWORD': 'pigs',
        'HOST': ''
    }
}