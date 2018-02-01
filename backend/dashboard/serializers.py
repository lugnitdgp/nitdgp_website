from rest_framework import serializers
from dashboard.models import Section, Tile


class TileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tile
        fields = ('name', 'icon', 'row', 'link',)


class DashboardSerializer(serializers.ModelSerializer):

    section_name = serializers.ReadOnlyField(source='name')
    contents = TileSerializer(many=True, source='tile_set')

    class Meta:
        model = Section
        fields = ('section_name', 'priority', 'contents',)
