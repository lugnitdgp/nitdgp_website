from rest_framework import serializers
from faculty.models import *
from department.models import Faculty
from department.serializers import CourseSerializer

class FacultyDetailSerializer(serializers.ModelSerializer):

    teachings = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    publication = serializers.SerializerMethodField()
    books_and_patents = serializers.SerializerMethodField()
    work_experience = serializers.SerializerMethodField()
    awards_and_recognition = serializers.SerializerMethodField()
    administrative_responsibilities = serializers.SerializerMethodField()

    def get_teachings(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return CourseSerializer(info.first().teachings, many=True).data

    def get_education(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return info.first().education

    def get_projects(self, obj):
        info = GeneralInformation.objects.filter(faculty=obj.id)
        return info.first().projects

    def get_publication(self, obj):
        info = Publication.objects.filter(faculty=obj.id)
        return PublicationSerializer(info, many=True).data

    def get_books_and_patents(self, obj):
        info = BooksPatents.objects.filter(faculty=obj.id)
        return BookPatentSerializer(info, many=True).data

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
        'education', 'projects', 'publication', 'books_and_patents', 'teachings', 'work_experience', 'awards_and_recognition',
        'administrative_responsibilities')


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = ('authors', 'title', 'journal', 'year_or_volume')


class BookPatentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksPatents
        fields = ('title', 'file', 'url')
