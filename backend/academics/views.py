from rest_framework.generics import ListAPIView, RetrieveAPIView
from academics.serializers import *


class NoticeViewSet(ListAPIView):

    queryset = Notice.objects.all()
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


class DocumentViewSet(RetrieveAPIView):

    queryset = Document.objects.all()
    serializer_class = DocumentMainSerializer

    def get_object(self):
        return self.get_queryset()


class RegulationViewSet(ListAPIView):

    queryset = Regulation.objects.all().order_by('-updated_at')
    serializer_class = RegulationSerializer


class RegistrationViewSet(ListAPIView):

    queryset = Registration.objects.all().order_by('-updated_at')
    serializer_class = RegistrationSerializer
