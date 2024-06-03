from django.conf.urls.static import static
from django.urls import path

from kvatera import settings
from webapp.views import *
app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contatcts/', contacts, name='contacts'),
    path('objects-rent/', objects_rent, name='objects-rent'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
