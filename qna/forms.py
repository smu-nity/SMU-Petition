from django import forms
from qna.models import qna, QnA_Answer


class QnAForm(forms.ModelForm):
    class Meta:
        model = qna
        fields = ['subject', 'content', 'anonymous']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = QnA_Answer
        fields = ['content']
