from django.conf.urls import url, include

from department.views import DepartmentViewSet, FacultyViewSet

app_name = 'department'

urlpatterns = [
    url(r'^department/', DepartmentViewSet.as_view(), name='list-department'),
    url(r'^faculties/(?P<slug>[\w]+)/$', FacultyViewSet.as_view(), name='list-department-faculty')
]
