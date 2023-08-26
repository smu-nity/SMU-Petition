from django.contrib import admin

from qna.models import qna, QnA_Answer

# Register your models here.

admin.site.register(qna)
admin.site.register(QnA_Answer)