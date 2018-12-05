from django.conf.urls import url

from academics.views import *

app_name = 'academics'

urlpatterns = [

    url(r'^academics/notices/$', NoticeViewSet.as_view(), name='view-notices'),
    url(r'^academics/calendar/$', CalendarViewSet.as_view(), name='view-calendar'),
    url(r'^academics/admission/$', AdmissionViewSet.as_view(), name='view-admission'),
    url(r'^academics/document/$', DocumentViewSet.as_view(), name='view-document'),
    url(r'^academics/regulations/$', RegulationViewSet.as_view(), name='view-regulation'),
    url(r'^academics/examination/$', ExaminationViewSet.as_view(), name='view-examination'),
    url(r'^academics/registration/$', RegistrationViewSet.as_view(), name='view-registration'),
    url(r'^academics/fee/$', FeeViewSet.as_view(), name='view-fee'),
    url(r'^academics/convocation/$', ConvocationViewSet.as_view(), name='view-convocation'),
    url(r'^convocation-links/(?P<sets>[\d]+)/$', convocation_links, name="convocation-links"),

]
