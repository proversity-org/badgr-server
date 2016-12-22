"""
WSGI config for myproject project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# Django <= 1.7
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# Django >= 1.8
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()