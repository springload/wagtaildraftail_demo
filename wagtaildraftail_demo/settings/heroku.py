from __future__ import absolute_import, unicode_literals

import dj_database_url
import os

from .base import *


DEBUG = True

# Accept all hostnames, since we don't know in advance which hostname will be used for any given Heroku instance.
# IMPORTANT: Set this to a real hostname when using this in production!
# See https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'wagtaildraftail.herokuapp.com'
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
