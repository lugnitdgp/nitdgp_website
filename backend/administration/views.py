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

     def list(self, request, *args, **kwargs):
         return Response({"results": SenateSerializer(self.get_queryset(), many=True, context={"request": request}).data
         })


class BogAgendaViewSet(ListAPIView):

     queryset = BogAgenda.objects.all()
     serializer_class = BogAgendaSerializer

     def list(self, request, *args, **kwargs):
         return Response({'result': BogAgendaSerializer(self.get_queryset(), many=True, context={'request': request}).data
         })


class DeansViewSet(ListAPIView):

    queryset = Dean.objects.all()
    serializer_class = DeanSerializer

    def list(self, request, *args, **kwargs):
        deans = self.get_queryset().filter(role='Dean')
        associate_deans = self.get_queryset().filter(role='Associate Dean')
        return Response({'deans': DeanSerializer(deans, many=True, context={"request": request}).data,
                         'associate_deans': DeanSerializer(associate_deans, many=True, context={"request": request}).data
                         })


class HodViewSet(ListAPIView):

    serializer_class = HODSerializer
    queryset = HOD.objects.all().order_by('department__name')


class WardenViewSet(ListAPIView):

    queryset = Warden.objects.all()
    serializer_class = WardenSerializer

    def list(self, request, *args, **kwargs):
        result = {}
        for warden in self.get_queryset():
            role = warden.role
            if role in result:
                result[role].append(WardenSerializer(warden, context={"request": request}).data)
            else:
                result[role] = [WardenSerializer(warden, context={"request": request}).data]
        return Response({"wardens": result})


class BOGViewSet(ListAPIView):

    queryset = BOG.objects.all()
    serializer_class = BOGSerializer

    def list(self, request, *args, **kwargs):
        chairperson = self.get_queryset().filter(role='Chairperson')
        secretary = self.get_queryset().filter(role='Secretary')
        members = self.get_queryset().filter(role='Member')
        return Response({'chairperson': BOGSerializer(chairperson, many=True, context={"request": request}).data,
                         'secretary': BOGSerializer(secretary, many=True, context={"request": request}).data,
                         'member': BOGSerializer(members, many=True, context={"request": request}).data
                         })


class OfficerViewSet(ListAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
