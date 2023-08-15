from datetime import date
from petitions.models import Petition


def crontab_every_day():
    today = date.today()
    petitions = Petition.objects.filter(end_date__lte=today, status=1)

    print(today)
    for petition in petitions:
        petition.status = 4
        petition.save()
        print(petition)
