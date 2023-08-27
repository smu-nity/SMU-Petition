from django.urls import path
from qna import views

app_name = 'qna'

urlpatterns = [
    path('<int:QnA_id>/', views.QnA_detail, name='QnA_detail'),
    path('create/', views.QnA_create, name='QnA_create'),
    path('modify/<int:QnA_id>/', views.QnA_modify, name='QnA_modify'),
    path('delete/<int:QnA_id>/', views.QnA_delete, name='QnA_delete'),
    path('QnA_list', views.QnA_list, name='QnA_list'),

    path('answer/create/<int:qna_id>/', views.QnA_answer_create, name='answer_create'),
    path('answer/create/<int:qna_id>/<str:type>/', views.QnA_answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.QnA_answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.QnA_answer_delete, name='answer_delete'),
    path('answer/', views.QnA_answer, name='answer'),
]
