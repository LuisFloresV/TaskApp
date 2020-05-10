"""
Django settings for todo project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zr$@w#&c!u9#_e4-r4n5pgl722u9g#^onh-avzaxmh#g*y+)s+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ENVIRONMENT = 'production'

if ENVIRONMENT == 'production': 
    SECURE_BROWSER_XSS_FILTER = True # new
    X_FRAME_OPTIONS = 'DENY' # new
    SECURE_SSL_REDIRECT = True 
    SECURE_HSTS_SECONDS = 3600 # new 
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new 
    SECURE_HSTS_PRELOAD = True # new 
    SECURE_CONTENT_TYPE_NOSNIFF = True # new
    SESSION_COOKIE_SECURE = True # new 
    CSRF_COOKIE_SECURE = True # new
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    DEBUG = False

ALLOWED_HOSTS = ['peaceful-beach-08145.herokuapp.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'users.apps.UsersConfig',
    'pages.apps.PagesConfig', 
    'todoapp.apps.TodoappConfig',

    'allauth',
    'allauth.account',
    'crispy_forms',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'todo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

STATICFILES_FINDERS = [
     "django.contrib.staticfiles.finders.FileSystemFinder", 
     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
      ]

AUTH_USER_MODEL = 'users.CustomUser'

SITE_ID = 1

AUTHENTICATION_BACKENDS = ( 
    'django.contrib.auth.backends.ModelBackend', 
    'allauth.account.auth_backends.AuthenticationBackend', 
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


LOGIN_REDIRECT_URL = 'home' 
LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False 

ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = 'email' # new 
ACCOUNT_EMAIL_REQUIRED = True # new 
ACCOUNT_UNIQUE_EMAIL = True # new
ACCOUNT_EMAIL_VERIFICATION ='mandatory'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT =3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300
CRISPY_TEMPLATE_PACK = 'bootstrap4'


SENDGRID_API_KEY = os.getenv('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')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "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")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "naokodeveloper@gmail.com")