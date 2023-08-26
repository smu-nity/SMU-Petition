from django import forms
from qna.models import qna, QnA_Comment, QnA_Answer


class QnAForm(forms.ModelForm):
    class Meta:
        model = qna
        fields = ['subject', 'content', 'anonymous']


class CommentForm(forms.ModelForm):
    class Meta:
        model = QnA_Comment
        fields = ['content']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = QnA_Answer
        fields = ['content']
