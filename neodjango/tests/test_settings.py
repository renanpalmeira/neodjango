import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NEO4J_DATABASES = {
    'default' : {
        'HOST':'localhost',
        'PORT': 7474,
        'ENDPOINT': '/db/data',   
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'test_database.sqlite3')
    }
}

INSTALLED_APPS = (
    'neodjango', 
)

SECRET_KEY="shutupdjangowe'retryingtotesthere"

DEBUG = True