from .common import *
 
DEBUG = True
 
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
 
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