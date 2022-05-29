from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = '510ed88f1fcb46'
# EMAIL_HOST_PASSWORD = '1386c3e348dcbb'
# EMAIL_PORT = '2525'
# DOMAIN = 'localhost:8000'
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DOMAIN = env("DOMAIN")
DEFAULT_FROM_EMAIL = "info@real-estate.com"
SITE_NAME = "Real Estate"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'users': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("PG_HOST"),
        'PROT': env("PG_PORT"),
    }
}
