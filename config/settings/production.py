from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['hairsalon']

STATIC_ROOT = '/var/run/{}/static'.format(PROJECT_NAME)

# Media files updated by users
MEDIA_ROOT = '/var/run/{}/pics'.format(PROJECT_NAME)

################
# Authenticate #
################

# 実際にメールを送信
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# メールサーバーへの接続設定
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

############
# Security #
############

DOMAIN = env('DOMAIN')
CSRF_TRUSTED_ORIGINS = [DOMAIN]