from rest_framework import serializers
from faculty.models import *
from publication.models import *
from department.models import Faculty
from department.serializers import CourseSerializer
from publication.serializers import *
import collections

class FacultyDetailSerializer(serializers.ModelSerializer):

    teachings = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    journals = serializers.SerializerMethodField()
    conferences = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    books = serializers.SerializerMethodField()
    patents = serializers.SerializerMethodField()
    work_experience = serializers.SerializerMethodField()
    awards_and_recognition = serializers.SerializerMethodField()
    administrative_responsibilities = serializers.SerializerMethodField()

    def get_teachings(self, obj):
        info = Teachings.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().teachings

    def get_education(self, obj):
        info = Education.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().education

    def get_projects(self, obj):
        info = Projects.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().projects

    def get_journals(self, obj):
        info = Journal.objects.filter(faculty_id=obj.id)
        return JournalSerializer(info, many=True).data

    def get_conferences(self, obj):
        info = Conference.objects.filter(faculty_id=obj.id)
        return ConferenceSerializer(info, many=True).data

    def get_students(self, obj):
        info = Students.objects.filter(faculty_id=obj.id)
        return StudentSerializer(info, context=self.context, many=True).data

    def get_books(self, obj):
        info = Book.objects.filter(faculty_id=obj.id)
        return BookSerializer(info, context=self.context, many=True).data

    def get_patents(self, obj):
        info = Patent.objects.filter(faculty_id=obj.id)
        return PatentSerializer(info, context=self.context, many=True).data

    def get_work_experience(self, obj):
        info = WorkExperience.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().work_experience

    def get_awards_and_recognition(self, obj):
        info = AwardsAndRecognition.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().awards_and_recognition

    def get_administrative_responsibilities(self, obj):
        info = AdministrativeResponsibility.objects.filter(faculty_id=obj.id)
        if info.count() == 0:
            return {}
        else :
            return info.first().administrative_responsibilities

    class Meta:
        model = Faculty
        fields = ('name', 'research_interest', 'image', 'email', 'joining_year', 'designation',
        'education', 'projects', 'dept_short_code', 'students', 'journals', 'conferences', 'books', 'patents', 'teachings', 'work_experience', 'awards_and_recognition',
        'administrative_responsibilities')



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('title', 'file')
