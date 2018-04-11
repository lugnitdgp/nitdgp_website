from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from administration.serializers import *
from administration.models import *
from department.serializers import FacultySerializer
from department.models import *


class CommonViewSet(RetrieveAPIView):
    """Base class for chairperson, director, registrar."""
    queryset = FacultyRoles.objects.all()
    serializer_class = FacultySerializer

    def __init__(self, post):
        try:
            self.instance = self.queryset.get(role__name=post).faculty
            self.post = post
        except ObjectDoesNotExist:
            self.instance = None

    def _allowed_methods(self):
        return ['GET', ]

    def retrieve(self, request, *args, **kwargs):
        if self.instance:
            data = self.get_serializer(self.instance).data
            return Response({self.post.lower(): data})
        else:
            raise Http404()


class DirectorViewSet(CommonViewSet):

    def __init__(self):
        super().__init__("Director")


class ChairpersonViewSet(CommonViewSet):

    def __init__(self):
        super().__init__("Chairperson")


class RegistrarViewSet(CommonViewSet):

    def __init__(self):
        super().__init__("Registrar")


class BwcListViewSet(ListAPIView):

    queryset = BwcIfc.objects.filter(type='bwc')
    serializer_class = BwcIfcSerializer


class IfcListViewSet(ListAPIView):

    queryset = BwcIfc.objects.filter(type='ifc')
    serializer_class = BwcIfcSerializer

class SenateViewSet(ListAPIView):

     queryset = Senate.objects.all()
     serializer_class = SenateSerializer


class DeansViewSet(ListAPIView):

    queryset = Dean.objects.all()
    serializer_class = DeanSerializer


class HodViewSet(ListAPIView):

    serializer_class = HODSerializer
    hod_role = Roles.objects.filter(name='HOD')
    queryset = FacultyRoles.objects.filter(role=hod_role)


class BOGViewSet(ListAPIView):

    queryset = BOG.objects.all()
    serializer_class = BOGSerializer

    def list(self, request, *args, **kwargs):
        chairperson = self.get_queryset().filter(role='Chairperson')
        secretary = self.get_queryset().filter(role='Secretary')
        members = self.get_queryset().filter(role='Member')
        return Response({'chairperson': BOGSerializer(chairperson, many=True).data,
                         'secretary': BOGSerializer(secretary, many=True).data,
                         'member': BOGSerializer(members, many=True).data
                         })
