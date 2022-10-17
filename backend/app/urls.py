from django.urls import path, include
from garpixcms.urls import urlpatterns

urlpatterns = [
    path('', include('garpix_vacancy.urls', namespace='garpix_vacancy'))
] + urlpatterns
