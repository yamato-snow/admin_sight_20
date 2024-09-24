"""
Google App Engine (GAE) 向けの最小限の本番環境用 Django 設定。
"""

from .base import *
import os

# デバッグモードを無効化
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# アプリケーションが動作可能なホストを指定
ALLOWED_HOSTS = ['.appspot.com']

# Google Cloud SQL with PostgreSQL の設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '/cloudsql/' + os.getenv('INSTANCE_CONNECTION_NAME'),
        'PORT': '5432',
    }
}

# 静的ファイルの設定
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

# セキュリティ設定
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# SECRET_KEY を環境変数から取得
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}


# 環境変数のチェック
REQUIRED_ENVS = ['DB_NAME', 'DB_USER', 'DB_PASSWORD', 'INSTANCE_CONNECTION_NAME', 'DJANGO_SECRET_KEY']
for env in REQUIRED_ENVS:
    if env not in os.environ:
        raise Exception(f"Required environment variable {env} is not set.")