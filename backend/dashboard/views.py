from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from dashboard.models import Section
from dashboard.serializers import DashboardSerializer


class DashboardViewSet(ListAPIView):

    queryset = Section.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = (AllowAny, )
