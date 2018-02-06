from rest_framework.generics import ListAPIView
from academics.serializers import *


class NoticeViewSet(ListAPIView):

    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
