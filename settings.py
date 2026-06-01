import dj_database_url
from dotenv import load_dotenv
import os
load_dotenv()


DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
