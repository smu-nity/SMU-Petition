from datetime import date, datetime


def crontab_every_day():
    today = date.today()

    print(today)
    print(datetime.now())

crontab_every_day()
