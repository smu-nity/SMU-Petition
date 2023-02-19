from django.db import models
from django.contrib.auth.models import User

from accounts.models import Profile
from config.settings import CATEGORY_CHOICES, STATUS_CHOICES


class Petition(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    anonymous = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f'[{self.author}] {self.subject} ({self.create_date})'

    def author_name(self):
        user = self.author
        profile = Profile.objects.filter(user=user)
        if profile:
            return profile.first().name
        return '익명'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'[{self.petition.subject}] {self.content} ({self.create_date})'


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'[{self.author}] {self.petition.subject} ({self.create_date})'
