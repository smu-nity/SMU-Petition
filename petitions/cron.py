import os
import sys
from datetime import datetime
from django.core.wsgi import get_wsgi_application
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/app')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()
from petitions.models import Petition


def crontab_every_minute():
    print(datetime.now())
    for petition in Petition.objects.all():
        print(petition.end_date)
