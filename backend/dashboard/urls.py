from django.conf.urls import url, include

from dashboard.views import DashboardViewSet

app_name = 'dashboard'

urlpatterns = [
    url(r'^dashboard/', DashboardViewSet.as_view(), name='list-tile-content'),
]
