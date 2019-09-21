# -*- coding: utf-8 -*-
from .base import *
import dj_database_url

DATABASES[‘default’] = dj_database_url.config()

DEBUG = False

ALLOWED_HOSTS = [‘yourappname.herokuapp.com’, '0.0.0.0'] 
