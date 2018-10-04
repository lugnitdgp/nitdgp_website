from django.conf.urls import url

from administration.views import *

app_name = 'administration'

urlpatterns = [

    url(r'^administration/director/$', DirectorViewSet.as_view(), name='view-director'),
    url(r'^administration/chairperson/$', ChairpersonViewSet.as_view(), name='view-chairperson'),
    url(r'^administration/registrar/$', RegistrarViewSet.as_view(), name='view-registrar'),
    url(r'^administration/bog/$', BOGViewSet.as_view(), name='view-bog'),
    url(r'^administration/bogagenda/$', BogAgendaViewSet.as_view(), name='view-bogagenda'),
    url(r'^administration/bwc/$', BwcListViewSet.as_view(), name='list-bwc'),
    url(r'^administration/ifc/$', IfcListViewSet.as_view(), name='list-ifc'),
    url(r'^administration/senate/$', SenateViewSet.as_view(), name='list-senate'),
    url(r'^administration/deans/$', DeansViewSet.as_view(), name='list-deans'),
    url(r'^administration/hod/$', HodViewSet.as_view(), name='list-hods'),
    url(r'^administration/wardens/$', WardenViewSet.as_view(), name='list-wardens'),
    url(r'^administration/officers/$', OfficerViewSet.as_view(), name='list-officers'),

]
