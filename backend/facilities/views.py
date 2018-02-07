from rest_framework.generics import ListAPIView, RetrieveAPIView

from facilities.serializers import *
from facilities.models import *


class LibraryViewSet(RetrieveAPIView):

	queryset = Library.objects.all()
	serializer_class = LibrarySerializer

	def get_object(self):
		return self.queryset.first()


class EResourceViewSet(ListAPIView):

	queryset = EResource.objects.all()
	serializer_class = EResourceSerializer

class SACViewSet(RetrieveAPIView):

	queryset = SAC.objects.all()
	serializer_class = SACSerializer

	def get_object(self):
		return self.queryset.first()
