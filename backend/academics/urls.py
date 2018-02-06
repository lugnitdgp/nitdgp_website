from django.conf.urls import url

from academics.views import *

app_name = 'academics'

urlpatterns = [

    url(r'^academics/notices$', NoticeViewSet.as_view(), name='view-notices'),

]
