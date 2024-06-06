from django.conf.urls.static import static
from django.urls import path

from kvatera import settings
from webapp.views import *
app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('objects-rent/', objects_rent, name='objects-rent'),
    path('detail-full-width/', detail_full, name='detail-full-width'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
