from django.conf.urls import url, include

from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    url(r'^dashboard/$', DashboardViewSet.as_view(), name='list-tile-content'),
    url(r'^dashboard/carousel$', CarouselViewSet.as_view(), name='list-carousel'),
    url(r'^dashboard/events$', EventViewSet.as_view(), name='list-events'),
]
