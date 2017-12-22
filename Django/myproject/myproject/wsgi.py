"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
'''
import os

from django.core.wsgi import get_wsgi_application

# GETTING-STARTED: change 'myproject' to your project name:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()
'''
"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# GETTING-STARTED: change 'myproject' to your project name:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()


import os, sys
sys.path.append('/home/gavin/Desktop/DjangoForWulab/Django/myproject/')
sys.path.append('/home/gavin/Desktop/DjangoForWulab/Django/')
sys.path.append('/home/gavin/Desktop/DjangoForWulab/')
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()