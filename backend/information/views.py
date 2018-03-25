from rest_framework.generics import ListAPIView
from information.serializers import *
from information.models import *


class ReportViewSet(ListAPIView):

    queryset = Report.objects.all().order_by('-updated_at')
    serializer_class = ReportMainSerializer


class AccountViewSet(ListAPIView):

    queryset = Account.objects.all().order_by('-updated_at')
    serializer_class = AccountSerializer


class CareerViewSet(ListAPIView):

    queryset = Career.objects.all().order_by('-updated_at')
    serializer_class = CareerSerializer


class TenderViewSet(ListAPIView):

    queryset = Tender.objects.all().order_by('-updated_at')
    serializer_class = TenderSerializer


class TEQIPViewSet(ListAPIView):

    queryset = TEQIP.objects.all().order_by('-updated_at')
    serializer_class = TEQIPSerializer


class RTIViewSet(ListAPIView):

    queryset = RTI.objects.all().order_by('-updated_at')
    serializer_class = RTISerializer


class NIRFViewSet(ListAPIView):

    queryset = NIRF.objects.all().order_by('-updated_at')
    serializer_class = NIRFSerializer


class NBAViewSet(ListAPIView):

    queryset = NBA.objects.all().order_by('-updated_at')
    serializer_class = NBASerializer
