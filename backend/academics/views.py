from rest_framework.generics import ListAPIView, RetrieveAPIView
from academics.serializers import *


class NoticeViewSet(RetrieveAPIView):

    queryset = Notice.objects.all()
    serializer_class = NoticeMainSerializer


class NoticeCustomViewSet(ListAPIView):

    serializer_class = NoticeSerializer

    def get_queryset(self):
        ntype = self.kwargs['ntype']
        ntype = NoticeType.objects.get(notice_type=ntype)
        return Notice.objects.filter(notice_type=ntype).order_by('-date')


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
