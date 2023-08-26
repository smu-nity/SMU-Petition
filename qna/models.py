import pytz
from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile
from config.settings import TIME_ZONE


# Create your models here.
class qna(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_qna')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    anonymous = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'[{self.author}] {self.subject} ({self.create_date})'

    def author_name(self):
        user = self.author
        profile = Profile.objects.filter(user=user)
        if profile:
            return profile.first().name
        return '익명'

    def create_date_str(self):
        return time_format(self.create_date)

    def modify_date_str(self):
        return time_format(self.modify_date)


class QnA_Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    QnA = models.ForeignKey(qna, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'[{self.author}] {self.QnA.subject} ({self.create_date})'

    def create_date_str(self):
        return time_format(self.create_date)

    def modify_date_str(self):
        return time_format(self.modify_date)


def time_format(time):
    return time.astimezone(pytz.timezone(TIME_ZONE)).strftime("%m/%d %H:%M")


def date_format(time):
    return time.astimezone(pytz.timezone(TIME_ZONE)).strftime("%y-%m-%d")
