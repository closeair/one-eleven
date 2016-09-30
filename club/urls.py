from django.conf.urls import url
from django.contrib import admin

from club import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^application/$', views.application, name='application'),
  url(r'^thanks/$', views.thanks, name='thanks'),
  url(r'^public/$', views.public, name='public'),
  url(r'^insurance/$', views.insurance, name='insurance'),
  url(r'^vote/(?P<motion>\d+)/$', views.vote, name='vote'),
  url(r'^complete/$', views.complete, name='complete'),
]
