from rest_framework.generics import ListAPIView, RetrieveAPIView

from activities.serializers import *
from activities.models import *

class StudentViewSet(ListAPIView):

	queryset = StudentClub.objects.all()
	serializer_class = StudentClubSerializer


class FestivalViewSet(ListAPIView):

	queryset = Festival.objects.all()
	serializer_class = FestivalSerializer


class GrievanceCellViewSet(ListAPIView):

	queryset = GrievanceCell.objects.all()
	serializer_class = GrievanceCellSerializer


class SeminarEventViewSet(ListAPIView):

	queryset = SeminarEvent.objects.all()
	serializer_class = SeminarEventSerializer


class AchievementsViewSet(ListAPIView):

	queryset = Achievement.objects.all()
	serializer_class = AchievementSerializer


class ResearchViewSet(ListAPIView):

	 queryset = Research.objects.all()
	 serializer_class = ResearchSerializer


class PlacementViewSet(ListAPIView):

	 queryset = Placement.objects.all()
	 serializer_class = PlacementSerializer


class VisitorViewSet(ListAPIView):

	queryset = Visitor.objects.all()
	serializer_class = VisitorSerializer


class PlacementLinksViewSet(ListAPIView):

	queryset = PlacementLinks.objects.all()
	serializer_class = PlacementLinksSerializer
