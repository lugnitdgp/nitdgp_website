from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from information.serializers import *
from information.models import *


class ReportViewSet(ListAPIView):

    queryset = Report.objects.all().order_by('-created_at')
    serializer_class = ReportSerializer

    def list(self, request, *args, **kwargs):
        result = {}
        for report in self.get_queryset():
            report_type = report.type
            try:
                result[report_type].append(ReportSerializer(report, context={"request": request}).data)
            except KeyError:
                result[report_type] = [ReportSerializer(report, context={"request": request}).data]
        return Response({"reports": result})


class AccountViewSet(ListAPIView):

    queryset = Account.objects.all().order_by('-created_at')
    serializer_class = AccountSerializer


class CareerViewSet(ListAPIView):

    queryset = Career.objects.all().filter(archive=False).order_by('-created_at')
    serializer_class = CareerSerializer

    def list(self, request, *args, **kwargs):
        return Response({"careers": CareerSerializer(self.get_queryset(), many=True, context={"request": request}).data })


class TenderViewSet(ListAPIView):

    queryset = Tender.objects.all().filter(archive=False).order_by('-created_at')
    serializer_class = TenderSerializer

    def list(self, request, *args, **kwargs):
        return Response({"tenders": TenderSerializer(self.get_queryset(), many=True, context={"request": request}).data })


class TEQIPViewSet(ListAPIView):

    queryset = TEQIP.objects.all().order_by('-created_at')
    serializer_class = TEQIPSerializer


class RTIViewSet(ListAPIView):

    queryset = RTI.objects.all().order_by('-created_at')
    serializer_class = RTISerializer


class NIRFViewSet(ListAPIView):

    queryset = NIRF.objects.all().order_by('-created_at')
    serializer_class = NIRFSerializer


class NBAViewSet(ListAPIView):

    queryset = NBA.objects.all().order_by('-created_at')
    serializer_class = NBASerializer


class OfficeNoticeViewSet(ListAPIView):

    queryset = OfficeNotice.objects.all().order_by('-created_at')
    serializer_class = OfficeNoticeSerializer


class MoreViewSet(ListAPIView):

    queryset = More.objects.all().order_by('-created_at')
    serializer_class = MoreSerializer


class PublicGrievanceViewSet(ListAPIView):
    queryset = PublicGrievance.objects.all().order_by('-date')
    serializer_class = PublicGrievanceSerializer


class ICCViewSet(ListAPIView):
    queryset = ICC.objects.all().order_by('-date')
    serializer_class = ICCSerializer

class NADViewSet(ListAPIView):
    queryset = NAD.objects.all().order_by('-date')
    serializer_class = NADSerializer
