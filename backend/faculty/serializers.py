from rest_framework import serializers
from faculty.models import *
from department.models import Faculty
from department.serializers import CourseSerializer
import collections

class FacultyDetailSerializer(serializers.ModelSerializer):

    teachings = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    publication = serializers.SerializerMethodField()
    conference = serializers.SerializerMethodField()
    publication_pdf = serializers.SerializerMethodField()
    conference_pdf = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    books_and_patents = serializers.SerializerMethodField()
    work_experience = serializers.SerializerMethodField()
    awards_and_recognition = serializers.SerializerMethodField()
    administrative_responsibilities = serializers.SerializerMethodField()

    def get_teachings(self, obj):
        info = GeneralInformation.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            #return CourseSerializer(info.first().teachings, many=True).data
            result = collections.defaultdict(list)
            teachings = info.first().teachings
            for course in teachings.order_by('semester'):
                    result[course.semester].append(CourseSerializer(course).data)
            return result

    def get_education(self, obj):
        info = GeneralInformation.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().education

    def get_projects(self, obj):
        info = GeneralInformation.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().projects

    def get_publication(self, obj):
        info = Publication.objects.filter(faculty_id=obj.id)
        return PublicationSerializer(info, many=True).data

    def get_conference(self, obj):
        info = Conference.objects.filter(faculty_id=obj.id)
        return ConferenceSerializer(info, many=True).data

    def get_publication_pdf(self, obj):
        info = PublicationPDF.objects.filter(faculty_id=obj.id)
        return PublicationPDFSerializer(info, many=True).data

    def get_conference_pdf(self, obj):
        info = ConferencePDF.objects.filter(faculty_id=obj.id)
        return ConferencePDFSerializer(info, many=True).data

    def get_students(self, obj):
        info = Students.objects.filter(faculty_id=obj.id)
        return StudentSerializer(info, context=self.context, many=True).data

    def get_books_and_patents(self, obj):
        info = BooksPatents.objects.filter(faculty_id=obj.id)
        return BookPatentSerializer(info, context=self.context, many=True).data

    def get_work_experience(self, obj):
        info = GeneralInformation.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().work_experience

    def get_awards_and_recognition(self, obj):
        info = GeneralInformation.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().awards_and_recognition

    def get_administrative_responsibilities(self, obj):
        info = GeneralInformation.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().administrative_responsibilities

    class Meta:
        model = Faculty
        fields = ('name', 'research_interest', 'image', 'email', 'joining_year', 'designation',
        'education', 'projects', 'dept_short_code', 'students', 'publication', 'books_and_patents', 'teachings', 'work_experience', 'awards_and_recognition',
        'administrative_responsibilities')


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = ('authors', 'title', 'journal', 'year_or_volume')


class ConferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conference
        fields = ('authors', 'title', 'location', 'year_or_volume')


class PublicationPDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicationPDF
        fields = ('publication', )


class ConferencePDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConferencePDF
        fields = ('conference', )


class BookPatentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksPatents
        fields = ('title', 'file', 'url')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('title', 'file')
