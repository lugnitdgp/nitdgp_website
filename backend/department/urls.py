from django.conf.urls import url

from department.views import *

app_name = 'department'

urlpatterns = [

    url(r'^department/$', DepartmentListViewSet.as_view(), name='list-department'),
    url(r'^department/(?P<pk>[\w-]+)/$', DepartmentViewSet.as_view(), name='view-department'),
    #url(r'^faculty/(?P<slug>[\w-]+)/$', FacultyViewSet.as_view(), name='list-department-faculty'),

]
