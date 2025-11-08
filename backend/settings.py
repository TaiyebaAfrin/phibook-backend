from pathlib import Path
import os
#import cloudinary
from decouple import config
import dj_database_url
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nfzm9aiuu1-hpi7l2i(x^+9817!l+*d!35dhd_k8cl@5zqw*qf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    ".vercel.app", 
    "127.0.0.1", 
    "localhost",
    "phibook-backend.vercel.app",
    "phibook-frontend.vercel.app"
]

AUTH_USER_MODEL = 'base.MyUser'

# FIXED JWT Settings
SIMPLE_JWT = {
    "USER_ID_FIELD": 'username',
    # 'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    # 'ROTATE_REFRESH_TOKENS': True,
    # 'BLACKLIST_AFTER_ROTATION': True,
    # 'UPDATE_LAST_LOGIN': False,
    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': SECRET_KEY,
    # 'VERIFYING_KEY': None,
    # 'AUDIENCE': None,
    # 'ISSUER': None,
    # 'JWK_URL': None,
    # 'LEEWAY': 0,
    # 'AUTH_HEADER_TYPES': ('Bearer',),
    # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    # 'USER_ID_CLAIM': 'user_id',
    # 'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',
    # 'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
    # 'JTI_CLAIM': 'jti',
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
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

# FIXED REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'base.authenticate.CookiesAuthentication',  # Keep your custom auth if needed
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # MOVE THIS TO TOP
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# FIXED CORS Settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # "http://127.0.0.1:3000",
    'http://127.0.0.1:8000',
    "https://phibook-frontend.vercel.app",
    "https://phibook-backend.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Add these for better cookie handling
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    'http://127.0.0.1:8000',
    "https://phibook-frontend.vercel.app",
    "https://phibook-backend.vercel.app",
]

SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

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

# Database Configuration
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

# # Cloudinary Configuration
# cloudinary.config(
#     cloud_name=os.environ.get('cloud_name', 'dgumbh4a9'),
#     api_key=os.environ.get('cloudinary_api_key', '523797784699343'),
#     api_secret=os.environ.get('api_secret', '7_GEvn1f55gImfDZw7qmki56LrE'),
#     secure=True
# )

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Email Configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'taiyebaafrin32@gmail.com'
# EMAIL_HOST_PASSWORD = 'xtdo kgbz joum fzrn'



# EMAIL_HOST=smtp.gmail.com
# EMAIL_HOST_PASSWORD=xtdo kgbz joum fzrn
# EMAIL_HOST_USER=taiyebaafrin32@gmail.com 
# EMAIL_PORT=587
# EMAIL_USE_TLS=True

# BACKEND_URL = config("BACKEND_URL")
# FRONTEND_URL = config("FRONTEND_URL")