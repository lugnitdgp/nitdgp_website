from rest_framework.generics import ListAPIView
from academics.serializers import *


class NoticeViewSet(ListAPIView):

    queryset = Notice.objects.all().order_by('date')
    serializer_class = NoticeSerializer


class CalendarViewSet(ListAPIView):

    queryset = Calendar.objects.all().order_by('-year')
    serializer_class = CalendarSerializer
