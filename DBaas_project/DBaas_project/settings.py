"""
Django settings for DBaas_project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
from environs import Env

#LDAP Configurations
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

# Set up environs
env = Env()
env.read_env()

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ['172.16.1.190','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_prometheus',
    'rest_framework',
    'corsheaders',
    'userAuth_app',
    'project_api',
    'provider1_api',
    'ADSapp',
]

MIDDLEWARE = [
     'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
    
]
APPEND_SLASH = False

ROOT_URLCONF = 'DBaas_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'DBaas_project.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Media Included 
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

AUTH_TOKEN_MODEL = 'rest_framework.authtoken.models.Token'



# Old db  setting
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]
 
 
ldapGroupSearch = 'CN=Users,DC=os3,DC=com  '
 
 
AUTH_LDAP_SERVER_URI = 'ldap://10.0.0.2:389'
AUTH_LDAP_BIND_DN = 'CN=Administrator,CN=Users,DC=os3,DC=com'
AUTH_LDAP_BIND_PASSWORD = 'P@33w0rd'
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    ldapGroupSearch,  # Use ldapGroupSearchBase here
    ldap.SCOPE_SUBTREE,
    "(sAMAccountName=%(user)s)"
)
 
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("CN=Users,DC=example,DC=com", ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
 
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "giveName",
    "last_name": "sn",
    "email": "mail"
}


CORS_ALLOWED_ORIGINS = [  
    'http://localhost:8080',
    'http://172.16.1.190:8080',
]
REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': [

        'rest_framework.renderers.JSONRenderer',

        'rest_framework.renderers.BrowsableAPIRenderer',

    ]

}


PROMETHEUS_LATENCY_BUCKETS = (0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0, 25.0, 50.0, 75.0, float("inf"),)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'project_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/project.log',
            'formatter': 'verbose',
        },
        'cluster_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/cluster.log',
            'formatter': 'verbose',
        },
        'deletecluster_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/deletecluster.log',
            'formatter': 'verbose',
        },
        'login_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/login.log',
            'formatter': 'verbose',
        },
        'user_creation_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/user.log',
            'formatter': 'verbose',
        },
        'role_assignment_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/role.log',
            'formatter': 'verbose',
        },
        'rename_project_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/renameproject.log',
            'formatter': 'verbose',
        },
        # Add more handlers if needed
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} level={levelname} {message} ',
            # 'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'loggers': {
        'project_logger': {
            'handlers': ['project_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'cluster_logger': {
            'handlers': ['cluster_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'deletecluster_logger': {
            'handlers': ['deletecluster_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'login_logger': {
            'handlers': ['login_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'user_creation_logger': {
            'handlers': ['user_creation_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'role_assignment_logger': {
            'handlers': ['role_assignment_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'rename_project_logger': {
            'handlers': ['rename_project_file'],
            'level': 'INFO',
            'propagate': True,
        },
        # Add more loggers if needed
    },
}