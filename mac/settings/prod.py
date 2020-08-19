from .common import *
import dj_database_url
 
DEBUG = False
 
ALLOWED_HOSTS = ['.herokuapp.com']
 
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pl',
        'USER': 'tathagat1234',
        'PASSWORD': '@Tathagat1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
 
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)