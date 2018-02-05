from django.conf.urls import url

from administration.views import *

app_name = 'administration'

urlpatterns = [

    url(r'^administration/director$', DirectorViewSet.as_view(), name='view-director'),
    url(r'^administration/chairperson$', ChairpersonViewSet.as_view(), name='view-chairperson'),
    url(r'^administration/registrar$', RegistrarViewSet.as_view(), name='view-registrar'),

]
