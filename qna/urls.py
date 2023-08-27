from django.urls import path

from qna import views

app_name = 'qna'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
]
