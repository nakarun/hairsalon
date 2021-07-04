from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Media files updated by users
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

################
# Authenticate #
################

INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
]

# This will avoid the need for an SMTP server as e-mails will be printed to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
