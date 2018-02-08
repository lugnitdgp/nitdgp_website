from django.conf.urls import url

from academics.views import *

app_name = 'academics'

urlpatterns = [

    url(r'^academics/notices$', NoticeViewSet.as_view(), name='view-notices'),
    url(r'^academics/calendar$', CalendarViewSet.as_view(), name='view-notices'),
    url(r'^academics/admission$', AdmissionViewSet.as_view(), name='view-admission'),

]
