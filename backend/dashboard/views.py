from rest_framework.generics import ListAPIView
from rest_framework.response import Response
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


class ContactViewSet(ListAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        result = {}
        for contact in self.get_queryset():
            group = contact.group
            if group in result:
                result[group].append(ContactSerializer(contact, context={"request": request}).data)
            else:
                result[group] = [ContactSerializer(contact, context={"request": request}).data]
        return Response({"contact": result})
