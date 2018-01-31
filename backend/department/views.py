from rest_framework.generics import ListAPIView

from department.models import Departments
from department.serializers import DepartmentListSerializer


class DepartmentViewSet(ListAPIView):

    queryset = Departments.objects.all()
    serializer_class = DepartmentListSerializer