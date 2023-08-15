from datetime import datetime

from petitions.models import Petition


def crontab_every_minute():
    for petition in Petition.objects.all():
        print(petition.end_date)
        print(datetime.now())