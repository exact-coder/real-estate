from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'users': {
    #     'ENGINE': env("POSTGRES_ENGINE"),
    #     'NAME': env("POSTGRES_DB"),
    #     'USER': env("POSTGRES_USER"),
    #     'PASSWORD': env("POSTGRES_PASSWORD"),
    #     'HOST': env("PG_HOST"),
    #     'PROT': env("PG_PORT"),
    # }
}
