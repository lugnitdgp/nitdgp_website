from django.conf.urls import url

from faculty.views import *

app_name = 'faculty'

urlpatterns = [

    url(r'^faculty/(?P<pk>[0-9a-f-]+)/$', FacultyViewSet.as_view(), name='retrieve-faculty'),
    url(r'^faculty/notes/$', download_note, name='faculty-download-note'),

]
