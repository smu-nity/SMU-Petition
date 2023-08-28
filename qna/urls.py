from django.urls import path

from qna import views

app_name = 'qna'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
    path('create/', views.question_create, name='question_create'),
    path('modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
