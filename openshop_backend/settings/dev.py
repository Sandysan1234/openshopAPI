from .common import *

DEBUG = True;

SECRET_KEY= 'django-insecure-x3=uiw6ni^=oq!3e#h9!&#)hp6$3__5zu+f%$c(nkmr5f+8!+q'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}