
""" 
Local settings to be used for development purposes.
Development-specific settings include
DEBUG mode, log level, and activation of
developer tools like django-debug-toolbar.
"""
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]
