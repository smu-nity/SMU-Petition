from django.urls import path
from qna import views

app_name = 'qna'

urlpatterns = [
    path('<int:qna_id>/', views.QnA_detail, name='qna_detail'),
    path('create/', views.QnA_create, name='qna_create'),
    path('modify/<int:petition_id>/', views.QnA_modify, name='qna_modify'),
    path('delete/<int:petition_id>/', views.QnA_delete, name='qna_delete'),
    path('qna/', views.QnA_list, name='qna_list'),

    path('comment/create/<int:qna_id>/', views.QnA_comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', views.QnA_comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.QnA_comment_delete, name='comment_delete'),

    path('answer/create/<int:qna_id>/', views.QnA_answer_create, name='answer_create'),
    path('answer/create/<int:qna_id>/<str:type>/', views.QnA_answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.QnA_answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.QnA_answer_delete, name='answer_delete'),
    path('answer/', views.QnA_answer, name='answer'),
]
