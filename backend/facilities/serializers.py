from rest_framework import serializers
from facilities.models import *
import collections


class CentersSerializer(serializers.ModelSerializer):
        class Meta:
                model = Centers
                fields = ('title', 'file', 'url', 'date')


class LibrarySerializer(serializers.ModelSerializer):

	class Meta:
		model = Library
		fields = ('home','about','contact_us')


class ResourceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Resource
		fields = ('title','url')


class SACSerializer(serializers.ModelSerializer):

	class Meta:
		model = SAC
		fields = ('about','mission','vision','program_offered','other_activities','facility','contact_us','ach_url','rec_url')


class HostelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Hostel
		fields = ('name', )


class CIFSerializer(serializers.ModelSerializer):

	class Meta:
		model = CIF
		fields = ('equipment_name','equipment_desc','image')
