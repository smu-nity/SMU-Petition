from django.urls import path
from petitions import views

app_name = 'petitions'

urlpatterns = [
    path('<int:petition_id>/', views.petition_detail, name='petition_detail'),
    # path('create/', views.petition_create, name='petition_create'),   # 상명대학교 청원 운영 종료
    path('modify/<int:petition_id>/', views.petition_modify, name='petition_modify'),
    path('delete/<int:petition_id>/', views.petition_delete, name='petition_delete'),
    path('vote/<int:petition_id>/', views.petition_vote, name='petition_vote'),
    path('status/<str:status>/', views.petition_list, name='petition_list'),

    path('comment/create/<int:petition_id>/', views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),

    path('answer/create/<int:petition_id>/', views.answer_create, name='answer_create'),
    path('answer/create/<int:petition_id>/<str:type>/', views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
