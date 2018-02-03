from django.conf.urls import url

from department.views import *

app_name = 'department'

urlpatterns = [

    url(r'^department/$', DepartmentListViewSet.as_view(), name='list-department'),
    url(r'^department/(?P<pk>[\w-]+)/$', DepartmentViewSet.as_view(), name='view-department'),
    url(r'^department/(?P<pk>[\w-]+)/people$', PeopleViewSet.as_view(), name='view-people'),
    url(r'^faculty/(?P<slug>[\w-]+)/$', FacultyViewSet.as_view(), name='list-department-faculty'),
    url(r'^department/(?P<id>[\w-]+)/aboutus$', AboutUsViewSet.as_view(), name='retrieve-department-about'),
    url(r'^department/(?P<id>[\w-]+)/hod/$', HodViewSet.as_view(), name='retrieve-department-hod'),

]
