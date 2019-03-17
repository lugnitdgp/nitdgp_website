from django.conf.urls import url
from search.views import NoticeSearchViewSet
from search.views import FacultySearchViewSet

urlpatterns = [
    url(r'^notice/$', NoticeSearchViewSet.as_view(), name='search_view_notice'),
    url(r'^faculty/$', FacultySearchViewSet.as_view(), name='search_view_faculty'),
]
