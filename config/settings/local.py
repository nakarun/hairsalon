from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Media files updated by users
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
