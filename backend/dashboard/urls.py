from django.conf.urls import url, include

from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    url(r'^dashboard/$', DashboardViewSet.as_view(), name='list-tile-content'),
    url(r'^dashboard/quick-links/$', QuickLinksViewSet.as_view(), name='list-quick-links'),
    url(r'^dashboard/downloads/$', DownloadsViewSet.as_view(), name='list-downloads'),
    url(r'^dashboard/carousel/$', CarouselViewSet.as_view(), name='list-carousel'),
    url(r'^dashboard/events/$', EventViewSet.as_view(), name='list-events'),
    url(r'^dashboard/newsfeed/$', NewsFeedViewSet.as_view(), name='list-newsfeed'),
    url(r'^dashboard/contacts/$', ContactViewSet.as_view(), name='list-contact'),
    url(r'^dashboard/footer/$', FooterViewSet.as_view(), name='list-footer-content'),
]
