from .base import *

DEBUG = False

# upisati domen od sajta
ALLOWED_HOSTS = ['*']


CORS_ALLOWED_ORIGINS = [
    "https://sanjamuskistudio.web.app",
    "https://sanjammuskistudio.rs",
    "http://localhost:8080"

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
EMAIL_HOST_USER = 'sanjamuskistudio@gmail.com'
EMAIL_HOST_PASSWORD = 'toqhorrzaiimcnff'
# EMAIL_HOST_PASSWORD = 'MARIC001'
EMAIL_USE_TLS = True