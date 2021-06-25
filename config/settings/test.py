from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = []

STATIC_ROOT = '/var/run/{}/static'.format(PROJECT_NAME)

# Media files updated by users
MEDIA_ROOT = '/var/run/{}/pics'.format(PROJECT_NAME)
