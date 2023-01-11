from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),


    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/update', views.post_update, name='post_update'),
]
