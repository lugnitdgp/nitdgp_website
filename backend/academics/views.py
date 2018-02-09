from rest_framework.generics import ListAPIView, RetrieveAPIView
from academics.serializers import *


class NoticeViewSet(ListAPIView):

    queryset = Notice.objects.all().order_by('date')
    serializer_class = NoticeSerializer


class CalendarViewSet(ListAPIView):

    queryset = Calendar.objects.all().order_by('-year')
    serializer_class = CalendarSerializer


class AdmissionViewSet(RetrieveAPIView):

    queryset = Admission.objects.all()
    serializer_class = AdmissionMainSerializer

    def get_object(self):
        return self.get_queryset()


class ExaminationViewSet(ListAPIView):

    queryset = Examination.objects.all().order_by('-year')
    serializer_class = ExaminationSerializer
