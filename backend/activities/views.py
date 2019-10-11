from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from activities.serializers import *
from activities.models import *
from publication.models import *
from publication.serializers import *
from faculty.models import *
from faculty.serializers import *

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

	queryset = SeminarEvent.objects.all().filter(archive=False)
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

class CollaborationViewSet(ListAPIView):

	queryset = Collaboration.objects.all()
	serializer_class = CollaborationSerializer

	def list(self, request, *args, **kwargs):
		result = {}
		for collaboration in self.get_queryset():
			ctype = collaboration.type
			if ctype in result:
				result[ctype].append(CollaborationSerializer(collaboration, context={"request":request}).data)
			else:
				result[ctype] = [CollaborationSerializer(collaboration, context={"request":request}).data]
		return Response({"collaborations":result})

class BricsViewSet(ListAPIView):

	queryset = Brics.objects.all()
	serializer_class = BricsSerializer

class CoeViewSet(ListAPIView):

	queryset = Coe.objects.all()
	serializer_class = CoeSerializer
	
class CoecarouselViewSet(ListAPIView):

	queryset = Coecarousel.objects.all()
	serializer_class = CoecarouselSerializer

	def list(self, request, *args, **kwargs):
		result = {}
		for coecarousels in self.get_queryset():
			coetype = coecarousels.coe_type
			if coetype in result:
				result[coetype].append(CoecarouselSerializer(coecarousels, context={"request":request}).data)
			else:
				result[coetype] = [CoecarouselSerializer(coecarousels, context={"request":request}).data]
		return Response({"coecarousels":result})


class OutreachViewSet(RetrieveAPIView):

	queryset = Outreach.objects.all()
	serializer_class = OutreachMainSerializer

	def get_object(self):
		return self.get_queryset()

	def list(self, request, *args, **kwargs):
		return Response({"results": OutreachMainSerializer(self.get_queryset(), context={"request": request}).data
		})

class AlljournalViewSet(ListAPIView):
	queryset = Journal.objects.all().order_by('-year', '-created_at')
	serializer_class = JournalSerializer

class AllprojectViewSet(ListAPIView):
	queryset = Projects.objects.all().order_by('-status','-created_at')
	serializer_class = ProjectsSerializer

class AllpatentViewSet(ListAPIView):
	queryset = Patent.objects.all().order_by('patent_status', '-patent_filed_year', '-created_at')
	serializer_class = PatentSerializer