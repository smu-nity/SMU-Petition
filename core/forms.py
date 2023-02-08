from django import forms
from core.models import Petition, Comment, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['subject', 'content', 'category']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }