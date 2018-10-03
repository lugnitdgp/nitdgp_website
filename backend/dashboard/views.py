from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.admin.models import LogEntry
from dashboard.models import *
from dashboard.serializers import *


class DashboardViewSet(ListAPIView):

    queryset = Section.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = (AllowAny, )

    def __init__(self):
        if(HitCount.objects.count() == 0):
            hits = HitCount()
            hits.count = 1
        else:
            hits = HitCount.objects.all().first()
            hits.count = hits.count + 1
        hits.save()


class QuickLinksViewSet(ListAPIView):

    queryset = QuickLinks.objects.all()
    serializer_class = QuickLinksSerializer

    def list(self, request, *args, **kwargs):
        result = {}
        for link in self.get_queryset():
            group = link.category
            if group in result:
                result[group].append(QuickLinksSerializer(link, context={"request": request}).data)
            else:
                result[group] = [QuickLinksSerializer(link, context={"request": request}).data]
        return Response({"groups": result})


class DownloadsViewSet(ListAPIView):
    queryset = Downloads.objects.all().order_by('created_at')
    serializer_class = DownloadsSerializer



class CarouselViewSet(ListAPIView):

    queryset = Carousel.objects.all().order_by('created_at')
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
        return Response({"groups": result})


class FooterViewSet(ListAPIView):

    queryset = LogEntry.objects.all()

    def list(self, request, *args, **kwargs):
        hits = HitCount.objects.all().first()
        last_log = self.get_queryset().first()
        return Response({"last_updated": last_log.action_time, "hits": hits.count})
