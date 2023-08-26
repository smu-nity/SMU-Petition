from django.contrib import admin

from qna.models import qna, QnA_Comment, QnA_Answer

# Register your models here.

admin.site.register(qna)
admin.site.register(QnA_Comment)
admin.site.register(QnA_Answer)