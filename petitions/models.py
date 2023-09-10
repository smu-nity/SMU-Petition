from datetime import datetime

import pytz
from django.db import models
from django.contrib.auth.models import User

from accounts.models import Profile
from config.settings import CATEGORY_CHOICES, STATUS_CHOICES, TIME_ZONE, SUCCESS_VALUE


class Petition(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_petition')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    anonymous = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f'[{self.author}] {self.subject} ({self.create_date})'

    def author_name(self):
        if self.anonymous:
            return '익명'
        profile = Profile.objects.filter(user=self.author)
        if profile:
            return profile.first().name
        return self.author.username

    def create_date_str(self):
        return time_format(self.create_date)

    def modify_date_str(self):
        return time_format(self.modify_date)

    def end_date_str(self):
        return date_format(self.end_date)

    def period_str(self):
        return f'{date_format(self.create_date)} ~ {date_format(self.end_date)}'

    def d_day(self):
        return f'D-{(self.end_date.date() - datetime.now().date()).days}'

    def get_percentage(self):
        return 100 if self.voter.count() >= int(SUCCESS_VALUE) else (self.voter.count() * 100) // int(SUCCESS_VALUE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'[{self.petition.subject}] {self.content} ({self.create_date})'

    def create_date_str(self):
        return time_format(self.create_date)

    def modify_date_str(self):
        return time_format(self.modify_date)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='petition_answer')
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'[{self.author}] {self.petition.subject} ({self.create_date})'

    def create_date_str(self):
        return time_format(self.create_date)

    def modify_date_str(self):
        return time_format(self.modify_date)


def time_format(time):
    return time.astimezone(pytz.timezone(TIME_ZONE)).strftime("%m/%d %H:%M")


def date_format(time):
    return time.astimezone(pytz.timezone(TIME_ZONE)).strftime("%y.%m.%d")
