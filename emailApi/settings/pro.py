from .base import *

DEBUG = False

# upisati domen od sajta
ALLOWED_HOSTS = ['*']




DATABASES = {
    'default': {
    
    }
}

ROOT_URLCONF = 'emailApi.urls'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
   ),
   
}