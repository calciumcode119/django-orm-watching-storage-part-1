from dotenv import load_dotenv
import os
load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': os.environ['ENGINE'],
        'HOST': os.environ['HOST'],
        'PORT': os.environ['PORT'],
        'NAME': os.environ['NAME'],
        'USER': os.environ['USER'],
        'PASSWORD': os.environ['PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
