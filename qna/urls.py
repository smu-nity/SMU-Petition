from django.urls import path

from qna import views

app_name = 'qna'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
    path('create/', views.question_create, name='question_create'),
    path('modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('delete/<int:question_id>/', views.question_delete, name='question_delete'),

]
