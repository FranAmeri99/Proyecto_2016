
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kk^oq@9g5z5uo_fjz(e8lf=+cisi1wzu^ia9v*t3q%x8vjnxss'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'principal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysitio_loginRS.urls'

WSGI_APPLICATION = 'mysitio_loginRS.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mibase.db',
    }
}

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
TEMPLATE_DIRS = [BASE_DIR.child('templates')]


STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

AUTHENTICATION_BACKENDS=(
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL='/'
SOCIAL_AUTH_LOGIN_URL='/error/'


SOCIAL_AUTH_FACEBOOK_KEY = '760651867409372'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b95d225499c9771968e3e4beb9cec19a'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = '---'
SOCIAL_AUTH_TWITTER_SECRET = '---'

