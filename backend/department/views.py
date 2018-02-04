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

    hod_role = Roles.objects.filter(name='HOD')
    hods = Faculty.objects.filter(pk=FacultyRoles.objects.filter(role=hod_role).values_list('faculty'))
    queryset = Department.objects.all()
    permission_classes = (AllowAny, )

    def retrieve(self, request, short_code):
        try:
            filter_kwargs = {'short_code': short_code}
            department = get_object_or_404(self.queryset, **filter_kwargs)
            faculty = Faculty.objects.filter(department=department.id)
            department_hod = self.hods.filter(department=department.id)
            people = PeopleSerializer(faculty)
            about_us = AboutUsSerializer(department)
            hod = FacultySerializer(department_hod, many=True)
            programmes = ProgrammeSerializer(department)
            return Response({"people": people.data, "about_us": about_us.data, "hod": hod.data, "programmes": programmes.data})
        except Http404:
            raise

