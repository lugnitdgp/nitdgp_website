from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from department.serializers import *


class DepartmentListViewSet(ListAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = DepartmentListSerializer(queryset, many=True)
        return Response({"departments":serializer.data})


class FacultyViewSet(ListAPIView):

    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(department__short_code__iexact=args[0])
        serializer = FacultySerializer(queryset, many=True)
        return Response({"faculties":serializer.data})


class DepartmentViewSet(RetrieveAPIView):

    queryset = Department.objects.all()
    serializer_class = MainSerializer


