from rest_framework.generics import ListAPIView

from department.models import Department
from department.serializers import DepartmentListSerializer


class DepartmentViewSet(ListAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer