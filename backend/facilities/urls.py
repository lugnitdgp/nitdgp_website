from django.conf.urls import url

from facilities.views import *

app_name = 'facilities'

urlpatterns = [

    url(r'^facilities/library/$', LibraryViewSet.as_view(), name='view-library'),
    url(r'^facilities/question/$', SemesterquestionViewSet.as_view(), name='view-question'),
    url(r'^facilities/centers/$', CentersViewSet.as_view(), name='view-centers'),
    url(r'^facilities/resource/$', ResourceViewSet.as_view(), name='view-resource'),
    url(r'^facilities/sac/$', SACViewSet.as_view(), name='view-sac'),
    url(r'^facilities/cif/$',CIFViewSet.as_view(), name='view-cif'),
    url(r'^facilities/medicle/$',MediclebullViewSet.as_view(), name='view-medicle'),
    url(r'^facilities/hostels/$',HostelViewSet.as_view(), name='view-hostels'),
    url(r'^facilities/pcbd/$',PCBDViewSet.as_view(), name='view-pcbd'),
    url(r'^facilities/pcbdcomplaint/$',pcbdcomplaint, name='view-pcbdcomplaint'),
    url(r'^facilities/logocompetition/$',logocompetition, name='view-logocompetition'),
    ]
