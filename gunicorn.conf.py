import os

bind = '0.0.0.0:8000'
workers = 2
accesslog = '-'
errorlog = '-'
loglevel = 'info'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()