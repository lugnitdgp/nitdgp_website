from rest_framework import serializers
from facilities.models import *
import collections


class CentersSerializer(serializers.ModelSerializer):

    class Meta:
            model = Center
            fields = ('title', 'image', 'link', 'description')


class LibrarySerializer(serializers.ModelSerializer):

	class Meta:
		model = Library
		fields = ('home','about','contact_us')


class ResourceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Resource
		fields = ('title','url')



class SemesterquestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semesterquestion
        fields = ('title','file')


class SACSerializer(serializers.ModelSerializer):

	class Meta:
		model = SAC
		fields = ('about', 'mission', 'vision', 'program_offered', 'other_activities', 'facility', 'contact_us', 'image', 'ach_url', 'rec_url')


class HostelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Hostel
		fields = ('name', )


class CIFSerializer(serializers.ModelSerializer):

	class Meta:
		model = CIF
		fields = ('equipment_name','equipment_desc','image')


class PCBDSerializer(serializers.ModelSerializer):

	class Meta:
		model = PCBD
		fields = ('c_number','name','email','mobile','cat','address','complaint','replytxt','replyurl')


class LogocompSerializer(serializers.ModelSerializer):

	class Meta:
		model = Logocomp
		fields = ('name','guardian','mobile','email','logoimg')
