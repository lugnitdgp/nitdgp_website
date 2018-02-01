from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from department.models import Department, Faculty
from department.serializers import DepartmentListSerializer, FacultySerializer


class DepartmentViewSet(ListAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
    	queryset = self.get_queryset()
    	serializer = DepartmentListSerializer(queryset, many=True)
    	return Response({"departments":serializer.data})


class FacultyViewSet(ListAPIView):

    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (AllowAny,)

    def list(self, request, slug):
    	queryset = self.get_queryset().filter(department__short_code__iexact=slug)
    	serializer = FacultySerializer(queryset, many=True)
    	return Response({"faculties":serializer.data})
