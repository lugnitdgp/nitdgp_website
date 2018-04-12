from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from dashboard.models import *
from dashboard.serializers import *


class DashboardViewSet(ListAPIView):

    queryset = Section.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = (AllowAny, )


class CarouselViewSet(ListAPIView):

    queryset = Carousel.objects.all().order_by('-updated_at')
    serializer_class = CarouselSerializer


class EventViewSet(ListAPIView):

    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer


class NewsFeedViewSet(ListAPIView):

    queryset = NewsFeed.objects.all().order_by('-created_at')
    serializer_class = NewsFeedSerializer