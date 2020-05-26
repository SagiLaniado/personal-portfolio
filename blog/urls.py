from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),

    #if url after 'blog' has an int
    #then pass this int into blog_id and push to detail function in views
    path('<int:blog_id>/', views.detail, name='detail'),
]
