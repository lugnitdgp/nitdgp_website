from rest_framework import serializers
from dashboard.models import *


class QuickLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickLinks
        fields = ('title', 'file', 'link', 'category')


class DownloadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downloads
        fields = ('title', 'file')


class TileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tile
        fields = ('name', 'icon', 'row', 'column', 'link',)


class DashboardSerializer(serializers.ModelSerializer):

    section_name = serializers.ReadOnlyField(source='name')
    contents = TileSerializer(many=True, source='tile_set')

    class Meta:
        model = Section
        fields = ('section_name', 'priority', 'contents',)


class CarouselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carousel
        fields = ('primary_caption', 'secondary_caption', 'image')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('title', 'file')


class NewsFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsFeed
        fields = ('title', 'file', 'date', 'url')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('name', 'designation', 'contact')
