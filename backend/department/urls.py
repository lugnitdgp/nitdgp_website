from django.conf.urls import url, include

from department.views import DepartmentListViewSet, FacultyViewSet

app_name = 'department'

urlpatterns = [
    url(r'^department/', DepartmentListViewSet.as_view(), name='list-department'),
    #url(r'^department/(?P<slug>[\w]+)/$', DepartmentViewSet.as_view(), name='view-department'),
    url(r'^faculty/(?P<slug>[\w]+)/$', FacultyViewSet.as_view(), name='list-department-faculty'),
]
