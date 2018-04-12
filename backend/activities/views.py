from rest_framework.generics import ListAPIView, RetrieveAPIView

from activities.serializers import *
from activities.models import *

class StudentViewSet(ListAPIView):

	queryset = StudentClub.objects.all()
	serializer_class = StudentClubSerializer


class SeminarEventViewSet(ListAPIView):

	queryset = SeminarEvent.objects.all()
	serializer_class = SeminarEventSerializer



class AchievementsViewSet(ListAPIView):

	queryset = Achievement.objects.all()
	serializer_class = AchievementSerializer