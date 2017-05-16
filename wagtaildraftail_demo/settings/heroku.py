from __future__ import absolute_import, unicode_literals

import dj_database_url
import os

from .base import *


DEBUG = True

try:
    from .local import *
except ImportError:
    pass
