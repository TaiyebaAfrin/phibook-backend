from pathlib import Path
import os
#import cloudinary
from decouple import config
import dj_database_url



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nfzm9aiuu1-hpi7l2i(x^+9817!l+*d!35dhd_k8cl@5zqw*qf'

# SECURITY WARNING: don't run with debug turned on in production!


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('SUPABASE_DB_NAME'),
#         'USER': os.environ.get('SUPABASE_DB_USER'),
#         'PASSWORD': os.environ.get('SUPABASE_DB_PASSWORD'),
#         'HOST': os.environ.get('SUPABASE_DB_HOST'),
#         'PORT': os.environ.get('SUPABASE_DB_PORT', '5432'),
#     }
# }




DEBUG = False


ALLOWED_HOSTS = [".vercel.app", "127.0.0.1", 'https://phibook-backend.vercel.app',]


AUTH_USER_MODEL = 'base.MyUser'

SIMPLE_JWT = {
    "USER_ID_FIELD":'username'
}



# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'base'
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'base.authenticate.CookiesAuthentication',
    )
}





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    'https://phibook-backend.vercel.app',
]

CORS_ALLOW_CREDENTIALS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# # Read from environment variable
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL'),
#         conn_max_age=600,
#         conn_health_checks=True,
#     )
# }


# #support
# DATABASES = {
#     'default': dj_database_url.config( default="postgresql://postgres:NkvVEW9hzsK5z3iC@db.gmjfcwlvzssmrmemciat.supabase.co:5432/postgres",
#         conn_max_age=600,
#         ssl_require=True
#     )
# }




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': "postgres.gmjfcwlvzssmrmemciat",
#         'PASSWORD': 'NkvVEW9hzsK5z3iC',
#         'HOST': 'aws-1-us-east-1.pooler.supabase.com',
#         'PORT': 6543,
#         'OPTIONS': {
#             'sslmode': 'require',
#             'sslmode': 'verify-full',
#         },
#         'CONN_MAX_AGE': 600,  # Helpful for serverless
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.gmjfcwlvzssmrmemciat',
        'PASSWORD': 'NkvVEW9hzsK5z3iC',
        'HOST': 'aws-1-us-east-1.pooler.supabase.com',
        'PORT': '6543',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

#cloudinary Configuration


# cloudinary.config(
#     cloud_name=config('cloud_name'),
#     api_key=config('cloudinary_api_key'),
#     api_secret=config('api_secret'),
#     secure=True
# )


# cloudinary.config(
#     cloud_name=os.environ.get('cloud_name', 'dgumbh4a9'),
#     api_key=os.environ.get('cloudinary_api_key', '523797784699343'),
#     api_secret=os.environ.get('api_secret', '7_GEvn1f55gImfDZw7qmki56LrE'),
#     secure=True
# )


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



