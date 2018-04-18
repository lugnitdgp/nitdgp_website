from rest_framework import serializers
from faculty.models import *
from department.models import Faculty

class FacultyDetailSerializer(serializers.ModelSerializer):

    education = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    publication = serializers.SerializerMethodField()
    work_experience = serializers.SerializerMethodField()
    awards_and_recognition = serializers.SerializerMethodField()
    administrative_responsibilities = serializers.SerializerMethodField()

    def get_education(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return info.first().education

    def get_projects(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return info.first().projects

    def get_publication(self, obj):
        result = {}
        return result

    def get_work_experience(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return info.first().work_experience

    def get_awards_and_recognition(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return info.first().awards_and_recognition

    def get_administrative_responsibilities(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return info.first().administrative_responsibilities

    class Meta:
        model = Faculty
        fields = ('name', 'research_interest', 'image', 'email', 'joining_year', 'designation',
        'education', 'projects', 'publication', 'work_experience', 'awards_and_recognition',
        'administrative_responsibilities')
