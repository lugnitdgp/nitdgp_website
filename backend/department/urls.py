from django.conf.urls import url, include

from department.views import DepartmentViewSet

app_name = 'department'

urlpatterns = [
    url(r'^department/', DepartmentViewSet.as_view(), name='list-tile-content'),
]
