from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from facilities.serializers import *
from facilities.models import *


class LibraryViewSet(ListAPIView):

	queryset = Library.objects.all().order_by('-updated_at')[:1]
	serializer_class = LibrarySerializer


class ResourceViewSet(ListAPIView):

	queryset = Resource.objects.all()
	serializer_class = ResourceSerializer

	def list(self, request, *args, **kwargs):
		result = {}
		for resource in self.get_queryset():
			rtype = resource.type
			if rtype in result:
				result[rtype].append(ResourceSerializer(resource, context={"request": request}).data)
			else:
				result[rtype] = [ResourceSerializer(resource, context={"request": request}).data]
		return Response({"resources": result})


class SACViewSet(ListAPIView):

	queryset = SAC.objects.all().order_by('-updated_at')[:1]
	serializer_class = SACSerializer


class HostelViewSet(ListAPIView):
	queryset = Hostel.objects.all()
	serializer_class = HostelSerializer


class CIFViewSet(ListAPIView):
	queryset = CIF.objects.all()
	serializer_class = CIFSerializer
