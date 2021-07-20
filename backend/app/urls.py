from django.urls import path, include
from garpixcms.urls import urlpatterns

urlpatterns = [
    path('vacancy/', include('garpix_vacancy.urls')),
] + urlpatterns
