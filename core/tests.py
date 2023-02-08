import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()
from core.models import Petition
from django.contrib.auth.models import User

user = User.objects.get(pk=1)
for i in range(300):
    q = Petition(author=user, subject='테스트 데이터입니다:[%03d]' % i, content='내용무')
    q.save()
