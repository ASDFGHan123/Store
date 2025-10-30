from .common import *


DEBUG = True


SECRET_KEY = 'django-insecure-0_xl!tam@0-8^rqfe7q6_in=bbf@m!ve2rf76r2a7dcq6+ch1q'

DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '12341234'
    }
}
