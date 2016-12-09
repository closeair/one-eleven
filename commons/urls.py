from django.conf.urls import url
from django.contrib import admin

from commons import views

urlpatterns = [
  url(r'^upload/$', views.upload, name='upload'),
  url(r'^uploaded/$', views.uploaded, name='uploaded'),
  url(r'^fleet/$', views.fleet, name='fleet'),
]
