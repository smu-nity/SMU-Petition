from datetime import datetime

from petitions.models import Petition


def crontab_every_minute():
    print(datetime.now())
    for petition in Petition.objects.all():
        print(petition.end_date)
