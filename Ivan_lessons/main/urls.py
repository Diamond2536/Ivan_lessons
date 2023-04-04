from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r'^lesson/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.lesson, name = 'lesson'),
]