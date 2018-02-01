from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from department.models import Department
from department.serializers import DepartmentListSerializer


class DepartmentViewSet(ListAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
    	queryset = self.get_queryset()
    	serializer = DepartmentListSerializer(queryset, many=True)
    	return Response({"departments":serializer.data})