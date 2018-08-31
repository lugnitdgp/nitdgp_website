from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from faculty.serializers import *
from department.models import Faculty


class FacultyViewSet(RetrieveAPIView):

    queryset = Faculty.objects.all()
    serializer_class = FacultyDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response({"faculty": FacultyDetailSerializer(self.get_queryset().filter(id=kwargs['pk']), many=True, context={'request': request}).data
                       })
