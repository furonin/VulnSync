import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'vulnsync_core' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vulnsync_core.settings')

application = get_wsgi_application()