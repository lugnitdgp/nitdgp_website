from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from department.serializers import *
from department.models import *

from django.http import Http404
from django.shortcuts import get_object_or_404


class DepartmentListViewSet(ListAPIView):

    queryset = Department.objects.all().order_by('short_code')
    serializer_class = DepartmentListSerializer
    permission_classes = (AllowAny, )

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DepartmentListSerializer(queryset, many=True)
        return Response({"departments": serializer.data})


class FacultyViewSet(ListAPIView):

    queryset = Department.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (AllowAny, )

    def list(self, request, slug):
        department = self.get_queryset().filter(short_code__iexact=slug).first()
        queryset = department.faculty_set.all()
        serializer = FacultySerializer(queryset, many=True)
        return Response({"faculties": serializer.data})


class DepartmentViewSet(RetrieveAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def retrieve(self, request, pk):
        import pdb
        pdb.set_trace()
        queryset = self.get_queryset().filter(short_code__iexact=pk)
        serializer = DepartmentSerializer(queryset, many=True)
        return Response({"details": serializer.data})


class AboutUsViewSet(RetrieveAPIView):

    queryset = Department.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = (AllowAny, )

    def retrieve(self, request, id):
        try:
            filter_kwargs = {'id': id}
            queryset = get_object_or_404(self.queryset, **filter_kwargs)
            serializer = AboutUsSerializer(queryset)
            return Response({"about-us": serializer.data})
        except Http404:
            raise


class HodViewSet(RetrieveAPIView):

    queryset = Faculty.objects.all()
    serializer_class = HodSerializer
    permission_classes = (AllowAny, )

    def retrieve(self, request, id):
        try:
            filter_kwargs = {'department_id' : id}
            queryset = get_object_or_404(self.queryset, **filter_kwargs)
            serializer = HodSerializer(queryset)
            return Response({"hod": serializer.data})
        except Http404:
            raise
