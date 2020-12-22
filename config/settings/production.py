""" 
Production settings settings to be used for production
This is the settings file used to host front-desk live in
production server. That is, the settings 
for the server that host the real live website
"""
from .base import *

# replace data with env var for V2 !!!
SECRET_KEY = "iz0(aw4pnd17tz&-m)n0t#1is_HAMPYcampyyu=z6_!r-e@df81cqf%v*@"

ALLOWED_HOSTS = []

DEBUG = False