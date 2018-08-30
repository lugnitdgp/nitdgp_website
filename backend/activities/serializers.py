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
