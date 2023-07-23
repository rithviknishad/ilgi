import dj_database_url
from corsheaders.defaults import default_headers

from .env import ABS_PATH, ENV_BOOL, ENV_INT, ENV_LIST, ENV_STR

DEBUG = ENV_BOOL("DEBUG", False)
SECRET_KEY = ENV_STR("SECRET_KEY", "secret" if DEBUG else "")
ALLOWED_HOSTS = ENV_LIST("ALLOWED_HOSTS", ",", ["*"] if DEBUG else [])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # project
    "ilgi.apps.IlgiConfig",
    "users.apps.UsersConfig",
    "utils.apps.UtilsConfig",
    "openapi.apps.OpenAPIConfig",
    # third party
    "dry_rest_permissions",
    "drf_spectacular",
    "django_filters",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {"default": dj_database_url.config(conn_max_age=600, ssl_require=not DEBUG)}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa: E501
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# allauth settings
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGOUT_ON_PASSWORD_CHANGE = False
LOGIN_REDIRECT_URL = "/"

REST_AUTH = {
    "SESSION_LOGIN": False,
}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

# static and media
STATIC_URL = ENV_STR("STATIC_URL", "/static/")
STATIC_ROOT = ENV_STR("STATIC_ROOT", ABS_PATH("static"))
MEDIA_URL = ENV_STR("MEDIA_URL", "/media/")
MEDIA_ROOT = ABS_PATH(ENV_STR("MEDIA_ROOT", "media"))

# email settings
EMAIL_BACKEND = "django.core.mail.backends.{}.EmailBackend".format(
    ENV_STR("EMAIL_BACKEND", "console" if DEBUG else "smtp")
)
EMAIL_HOST = ENV_STR("EMAIL_HOST", "localhost")
EMAIL_HOST_USER = ENV_STR("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = ENV_STR("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = ENV_INT("EMAIL_PORT", 25)
EMAIL_USE_TLS = ENV_BOOL("EMAIL_USE_TLS", False)
SERVER_EMAIL = ENV_STR("SERVER_EMAIL", "webmaster@localhost")
DEFAULT_FROM_EMAIL = ENV_STR("DEFAULT_FROM_EMAIL", SERVER_EMAIL)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": ENV_STR("THROTTLE_ANONYMOUS", "100/hour"),
        "user": ENV_STR("THROTTLE_AUTHENTICATED", "1000/hour"),
    },
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# log to console, assume the supervisor/system runner will take care of the logs
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": ENV_STR("LOG_LEVEL", "INFO"),
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = default_headers + ("content-disposition",)

CELERY_BROKER_URL = ENV_STR("CELERY_BROKER_URL", "amqp://localhost")
CELERY_BACKEND = ENV_STR("CELERY_BACKEND")
CELERY_ALWAYS_EAGER = ENV_BOOL("CELERY_ALWAYS_EAGER", False)

# Periodic tasks via Celery Beat
# See https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#beat-entries
CELERY_BEAT_SCHEDULE = {}

if ENV_BOOL("USE_X_FORWARDED_PROTO"):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = ENV_BOOL("USE_X_FORWARDED_HOST")
USE_X_FORWARDED_PORT = ENV_BOOL("USE_X_FORWARDED_PORT")

SPECTACULAR_SETTINGS = {
    "TITLE": "ilgi",
    "DESCRIPTION": """Life, routines, mental & physical health tracker.""",
    "VERSION": "0.5",
    "SERVE_INCLUDE_SCHEMA": False,
}
