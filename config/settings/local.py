from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Media files updated by users
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

################
# Authenticate #
################

# This will avoid the need for an SMTP server as e-mails will be printed to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
