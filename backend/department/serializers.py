from rest_framework import serializers
from department.models import *
import collections


class DepartmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name', 'short_code',)


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ('name', 'designation', 'image')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('title', 'file')


class SyllabusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Syllabus
        fields = ('title', 'file')


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ('id', 'name', 'research_interest', 'email', 'designation', 'mobile', 'joining_year', 'image')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ('title', 'short_code', 'l', 't', 's', 'credits')


class ResearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Research
        fields = ('collab_inst', 'area', 'faculty_involved', 'date')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('collab_inst', 'area', 'faculty_involved', 'funding', 'date')


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('speakers', 'programme', 'start_date', 'end_date')


class DepartmentPhotosSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartmentPhotos
        fields = ('title', 'image')


class DepartmentNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartmentNews
        fields = ('title', 'link', 'date')


class PeopleSerializer(serializers.ModelSerializer):

    faculty = serializers.SerializerMethodField()
    staff = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    def get_faculty(self, obj):
        faculty_list = Faculty.objects.filter(department=self.context['obj'].id)
        faculty_list = sorted(faculty_list, key=lambda x: x.name.split()[-1])
        data = FacultySerializer(faculty_list, many=True, context=self.context).data

        return data

    def get_staff(self, obj):
        staff_list = Staff.objects.filter(department=self.context['obj'].id)
        return StaffSerializer(staff_list, many=True, context=self.context).data

    def get_students(self, obj):
        student_list = Student.objects.filter(department=self.context['obj'].id)
        return StudentSerializer(student_list, many=True, context=self.context).data

    class Meta:
        model = Faculty
        fields = ('faculty', 'staff', 'students')


class MainSerializer(serializers.ModelSerializer):

    def get_hod(self, obj):

        hod_role = Roles.objects.filter(name='HOD')
        for faculty_role in HOD.objects.all():
            faculty_department = faculty_role.department
            if faculty_department.id == obj.id:
                department_hod = faculty_role.faculty
                return FacultySerializer(department_hod, context=self.context).data
        return {}

    def get_people(self, obj):

        faculty = Faculty.objects.filter(department=obj.id)
        return PeopleSerializer(faculty, context={'request': self.context['request'], 'obj': obj}).data

    def get_programmes(self, obj):

        result = collections.defaultdict()
        for i in self.instance.programme_set.all():

            try:
                result[i.degree.name].append({
                    'programme_title': i.title
                })
            except KeyError:
                result[i.degree.name] = [{
                    'programme_title': i.title
                }]
            for semester in i.courses_set.values('semester').order_by('semester'):

                for j in result[i.degree.name]:

                    if j['programme_title'] == i.title:

                        j[semester['semester']] = CourseSerializer(
                          i.courses_set.filter(
                            semester=semester['semester']
                             ), many=True
                          ).data
        return result

    def get_facilities(self, obj):

        result = collections.defaultdict()
        departmental_facilities = Facility.objects.filter(department=obj.id)
        for facility in departmental_facilities:
            try:
                result[facility.category].append({'name': facility.name})
            except KeyError:
                result[facility.category] = [{'name': facility.name}]

        return result

    def get_syllabus(self, obj):
        result = collections.defaultdict()
        syllabus = Syllabus.objects.filter(department=obj.id)
        for i in syllabus:
            try:
                result[i._degree()].append(SyllabusSerializer(i, context=self.context,).data)
            except KeyError:
                result[i._degree()] = [SyllabusSerializer(i, context=self.context,).data]
        return result

    def get_research(self, obj):

        research = Research.objects.filter(department=obj.id)
        return ResearchSerializer(research, context=self.context, many=True).data

    def get_projects(self, obj):

        projects = Project.objects.filter(department=obj.id)
        return ProjectSerializer(projects, context=self.context, many=True).data

    def get_activities(self, obj):

        activity = Activity.objects.filter(department=obj.id)
        return ActivitySerializer(activity, context=self.context, many=True).data

    def get_photos(self, obj):

        photo = DepartmentPhotos.objects.filter(department=obj.id)
        return DepartmentPhotosSerializer(photo, context=self.context, many=True).data

    def get_news(self, obj):

        news = DepartmentNews.objects.filter(department=obj.id)
        return DepartmentNewsSerializer(news, context=self.context, many=True).data

    hod = serializers.SerializerMethodField()
    people = serializers.SerializerMethodField()
    programmes = serializers.SerializerMethodField()
    facilities = serializers.SerializerMethodField()
    research = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()
    news = serializers.SerializerMethodField()
    syllabus = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('name', 'short_code', 'about_us', 'mission', 'vision', 'contact_us', 'hod', 'people', 'programmes', 'research', 'projects', 'activities', 'facilities', 'photos', 'news', 'syllabus')
