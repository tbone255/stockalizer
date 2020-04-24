"""
WSGI config for stockalyzer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv, find_dotenv

if os.getenv('PRODUCTION') is None:
    load_dotenv(find_dotenv())
    print(os.getenv('TEST'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockalyzer.settings')

application = get_wsgi_application()
