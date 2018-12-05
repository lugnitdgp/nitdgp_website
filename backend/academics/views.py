from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from academics.serializers import *
from django.http import HttpResponse
from pathlib import Path
from os import listdir
import json

class NoticeViewSet(ListAPIView):

    queryset = Notice.objects.all().filter(archive=False).order_by('-date')
    serializer_class = NoticeSerializer

    def list(self, request, *args, **kwargs):
        result = {}
        for notice in self.get_queryset():
            ntype = notice.notice_type
            if ntype in result:
                result[ntype].append(NoticeSerializer(notice, context={"request": request}).data)
            else:
                result[ntype] = [NoticeSerializer(notice, context={"request": request}).data]
        return Response({"notices": result})


class CalendarViewSet(ListAPIView):

    queryset = Calendar.objects.all().order_by('-year')
    serializer_class = CalendarSerializer


class ConvocationViewSet(ListAPIView):

    queryset = Convocation.objects.all()
    serializer_class = ConvocationSerializer


class AdmissionViewSet(ListAPIView):

    queryset = AdmissionDegree.objects.all()
    serializer_class = AdmissionMainSerializer


class ExaminationViewSet(ListAPIView):

    queryset = Examination.objects.all().order_by('-updated_at')
    serializer_class = ExaminationSerializer


class DocumentViewSet(RetrieveAPIView):

    queryset = Document.objects.all()
    serializer_class = DocumentMainSerializer

    def get_object(self):
        return self.get_queryset()


class RegulationViewSet(ListAPIView):

    queryset = Regulation.objects.all().order_by('-updated_at')
    serializer_class = RegulationSerializer


class FeeViewSet(ListAPIView):

    queryset = Fee.objects.all().order_by('-updated_at')
    serializer_class = FeeSerializer


class RegistrationViewSet(ListAPIView):

    queryset = Registration.objects.all().order_by('-updated_at')
    serializer_class = RegistrationSerializer


def convocation_links(request, sets):
        BASE_DIR = "/var/www/html/nitdgp_website/frontend/dist/convocation-photos/"
        sets = int(sets)
        x = {}
        for i in range(1, sets + 1):
                path = BASE_DIR + "SET" + str(i) + "-small"
                if Path(path).exists():
                        x[path.split("/")[-1]] = listdir(path)
        return HttpResponse(json.dumps(x), content_type="application/json")
