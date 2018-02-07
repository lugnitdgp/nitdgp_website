from django.conf.urls import url

from facilities.views import *

app_name = 'facilities'

urlpatterns = [

	url(r'^facilities/library$', LibraryViewSet.as_view(), name='view-library'),
	url(r'^facilities/eresource$', EResourceViewSet.as_view(), name='view-eresource'),
	url(r'^facilities/sac$', SACViewSet.as_view(), name='view-sac'),

	]
