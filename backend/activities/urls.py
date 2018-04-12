from django.conf.urls import url

from activities.views import *

app_name = 'activities'

urlpatterns = [

		url(r'^activities/student-clubs/$', StudentViewSet.as_view(), name='view-student-clubs'),
		url(r'^activities/seminars-and-events/$', SeminarEventViewSet.as_view(), name='view-seminars-events'),
		url(r'^activities/achievements/$', AchievementsViewSet.as_view(), name='view-achievements'),
    ]
