"""
開発環境用の Django 設定。
"""

from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Emメールバックエンドを使用して、コンソールに送信されたメールを表示する
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# デバッグツールバーを有効化
INSTALLED_APPS += ['debug_toolbar'] 
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']

# SECRET_KEYを環境変数から取得
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-development-key')