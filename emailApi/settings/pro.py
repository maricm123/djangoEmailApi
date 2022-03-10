from .base import *

DEBUG = False

# upisati domen od sajta
ALLOWED_HOSTS = ['*']


CORS_ALLOWED_ORIGINS = [
    "https://sanjamuskistudio.web.app",
]

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



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mihailomaric001@gmail.com'
EMAIL_HOST_PASSWORD = 'fgvflyjyvjzyidse'
EMAIL_USE_TLS = True