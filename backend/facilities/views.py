from rest_framework.generics import ListAPIView, RetrieveAPIView

from facilities.serializers import *
from facilities.models import *


class LibraryViewSet(ListAPIView):

	queryset = Library.objects.all().order_by('-updated_at')[:1]
	serializer_class = LibrarySerializer


class EResourceViewSet(ListAPIView):

	queryset = EResource.objects.all()
	serializer_class = EResourceSerializer


class SACViewSet(ListAPIView):

	queryset = SAC.objects.all().order_by('-updated_at')[:1]
	serializer_class = SACSerializer
