from rest_framework import serializers
from dashboard.models import Section, Content


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('name', 'icon', 'row', 'link',)


class DashboardSerializer(serializers.ModelSerializer):

    section_name = serializers.ReadOnlyField(source='name')
    contents = ContentSerializer(many=True, source='content_set')

    class Meta:
        model = Section
        fields = ('section_name', 'priority', 'contents',)