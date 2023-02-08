from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.petition_list, name='petition_list'),
    path('<int:petition_id>/', views.petition_detail, name='petition_detail'),

    path('petition/create/', views.petition_create, name='petition_create'),
    path('petition/modify/<int:petition_id>/', views.petition_modify, name='petition_modify'),
    path('petition/delete/<int:petition_id>/', views.petition_delete, name='petition_delete'),
    path('petition/vote/<int:petition_id>/', views.petition_vote, name='petition_vote'),

    path('comment/create/<int:petition_id>/', views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),

    path('answer/create/<int:petition_id>/', views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
