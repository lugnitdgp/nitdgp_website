from rest_framework.generics import ListAPIView

from dashboard.models import Section
from dashboard.serializers import DashboardSerializer


class DashboardViewSet(ListAPIView):

    queryset = Section.objects.all()
    serializer_class = DashboardSerializer
