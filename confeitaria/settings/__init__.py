"""
Django settings package for confeitaria project.
"""

from .base import *

# Import environment-specific settings
from decouple import config

env = config('DJANGO_ENVIRONMENT', default='development')

if env == 'production':
    from .production import *
else:
    from .development import *
