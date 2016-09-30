from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = 'RICHMOND PILOTS'

urlpatterns=[
   url(r'^', include('club.urls')),
   url(r'^', include('commons.urls')),
   url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
