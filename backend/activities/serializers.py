from rest_framework import serializers
from activities.models import *


class StudentClubSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentClub
		fields = ('name', 'link', 'image', 'description')


class FestivalSerializer(serializers.ModelSerializer):

	class Meta:
		model = Festival
		fields = ('name', 'link', 'image', 'description')


class GrievanceCellSerializer(serializers.ModelSerializer):

	class Meta:
		model = GrievanceCell
		fields = ('title', 'file', 'url', 'date')


class SeminarEventSerializer(serializers.ModelSerializer):

	class Meta:
		model = SeminarEvent
		fields = ('title', 'file', 'url', 'date')


class AchievementSerializer(serializers.ModelSerializer):

	class Meta:
		model = Achievement
		fields = ('title', 'file', 'date')


class ResearchSerializer(serializers.ModelSerializer):

	class Meta:
		model = Research
		fields = ('title', 'file', 'date', 'url')


class PlacementLinksSerializer(serializers.ModelSerializer):

	class Meta:
		model = PlacementLinks
		fields = ('title', 'file', 'date', 'url')


class PlacementSerializer(serializers.ModelSerializer):

	class Meta:
		model = Placement
		fields = ('title', 'file', 'date', 'url')


class VisitorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Visitor
		fields = ('name', 'designation', 'event_name', 'image')

class CollaborationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Collaboration
		fields = ('title', 'file', 'type', 'date', 'url')

class BricsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Brics
		fields = ('title', 'file', 'date')

class CoeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Coe
		fields = ('name', 'link', 'description', 'image')

class CoecarouselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coecarousel
        fields = ('primary_caption', 'coe_type', 'secondary_caption', 'image')


class OutreachSerializer(serializers.ModelSerializer):
	class Meta:
		model = Outreach
		fields = ('name', 'icon', 'mou')


class OutreachMainSerializer(serializers.ModelSerializer):
	def get_outreach(self, obj):
		result = {}
		for i in self.instance:
			value = OutreachSerializer(i, context=self.context).data
			try:
				result[i.category].append(value)
			except KeyError:
				result[i.category] = [value]
		return result
	outreach = serializers.SerializerMethodField()
	class Meta:
		model = Outreach
		fields = ('outreach',)


class NewsletterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Newsletter
		fields = ('title', 'file', 'link', 'date')