from django.conf.urls import url, include

from department.views import *

app_name = 'department'

urlpatterns = [
    #url(r'^department/(?P<slug>[\w]+)/$', DepartmentViewSet.as_view(), name='view-department'),
    url(r'^department/(?P<pk>[0-9a-f-]+)/$', DepartmentViewSet.as_view(), name='view-department'),
    # url(r'^department/$', DepartmentListViewSet.as_view(), name='list-department'),
    #
    # url(r'^faculty/(?P<slug>[\w]+)/$', FacultyViewSet.as_view(), name='list-department-faculty'),
]
