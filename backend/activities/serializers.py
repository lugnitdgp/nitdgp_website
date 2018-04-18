from rest_framework import serializers
from activities.models import *


class StudentClubSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentClub
		fields = ('name', 'link', 'image', 'description')


class SeminarEventSerializer(serializers.ModelSerializer):

	class Meta:
		model = SeminarEvent
		fields = ('title', 'file', 'date')


class AchievementSerializer(serializers.ModelSerializer):

	class Meta:
		model = Achievement
		fields = ('title', 'file', 'date')


class ResearchSerializer(serializers.ModelSerializer):

	class Meta:
		model = Research
		fields = ('title', 'file', 'date', 'url')
