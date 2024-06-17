"""
構成プロジェクトの Django 設定。

Django 3.2.8 を使用して 'django-admin startproject' によって生成されました。

このファイルの詳細については、以下を参照してください。

https://docs.djangoproject.com/en/3.2/topics/settings/

設定とその値の完全なリストについては、以下を参照してください。

https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Bプロジェクト内のビルド パスは、BASE_DIR / 'subdir' のようになります。.
BASE_DIR = Path(__file__).resolve().parent.parent


# クイックスタート開発設定 - 本番環境には適していません
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# セキュリティ警告: 本番環境で使用される秘密鍵は秘密にしておいてください。
SECRET_KEY = 'django-insecure-pqiye-1(ui^!y8-&6u9sqlv!c6ydj))&5xts!l+(@l=6-$8h96'

# セキュリティ警告: 本番環境ではデバッグをオンにして実行しないでください。
DEBUG = True

ALLOWED_HOSTS = []


# アプリケーション定義

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'regular.apps.RegularConfig', # 定期業務
    # 'book.apps.BookConfig', # 本管理
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookproject.wsgi.application'


# データベース
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# パスワードの検証
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 国際化
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# 静的ファイル（CSS、JavaScript、画像）
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# デフォルトの主キーフィールドタイプ
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'index'

LOGOUT_REDIRECT_URL = 'index'