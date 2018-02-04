from rest_framework.generics import ListAPIView, RetrieveAPIView

from department.serializers import *
from department.models import *


class DepartmentListViewSet(ListAPIView):

    queryset = Department.objects.all().order_by('short_code')
    serializer_class = DepartmentListSerializer


class FacultyViewSet(ListAPIView):

    queryset = Department.objects.all()
    serializer_class = FacultySerializer


class DepartmentViewSet(RetrieveAPIView):

    queryset = Department.objects.all()
    serializer_class = MainSerializer


