from datetime import date, datetime
from petitions.models import Petition


def crontab_every_day():
    petitions = Petition.objects.filter(end_date__lte=date.today(), status=1)
    print(datetime.now())
    for petition in petitions:
        petition.status = 4
        petition.save()
        print(petition)
