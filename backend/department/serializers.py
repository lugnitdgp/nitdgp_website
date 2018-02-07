from rest_framework import serializers
from department.models import *
import collections


class DepartmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name', 'short_code',)


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ('name', 'research_interest', 'email', 'mobile', 'joining_year')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ('title', 'short_code', 'semester', 'course_type', 'credits',)


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
        fields = ('title', 'link')


class FacultyRolesSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='faculty.name')
    email = serializers.ReadOnlyField(source='faculty.email')
    mobile = serializers.ReadOnlyField(source='faculty.mobile')
    research_interest = serializers.ReadOnlyField(source='faculty.research_interest')
    joining_year = serializers.ReadOnlyField(source='faculty.joining_year')

    class Meta:

        model = FacultyRoles
        fields = ('name', 'email', 'mobile', 'research_interest', 'joining_year')


class PeopleSerializer(serializers.ModelSerializer):

    faculty = serializers.SerializerMethodField()

    def get_faculty(self, obj):
        result = collections.defaultdict()
        for role in Roles.objects.filter(type='Departmental'):
            faculty_list = role.facultyroles_set.filter(faculty__department=self.context.id)
            data = FacultyRolesSerializer(faculty_list, many=True).data
            if len(data) != 0 and role.name != 'HOD':
                result[role.name] = data

        return result

    class Meta:
        model = Faculty
        fields = ('faculty', )


class MainSerializer(serializers.ModelSerializer):

    def get_hod(self, obj):

        hod_role = Roles.objects.filter(name='HOD')
        for faculty_role in FacultyRoles.objects.filter(role=hod_role):
            faculty_department = faculty_role.faculty.department
            if faculty_department.id == obj.id:
                department_hod = faculty_role.faculty
                return FacultySerializer(department_hod).data
        return {}

    def get_people(self, obj):

        faculty = Faculty.objects.filter(department=obj.id)
        return PeopleSerializer(faculty, context=obj).data

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

                        j['semester '+str(semester['semester'])] = CourseSerializer(
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

    def get_research(self, obj):

        research = Research.objects.filter(department=obj.id)
        return ResearchSerializer(research, many=True).data

    def get_projects(self, obj):

        projects = Project.objects.filter(department=obj.id)
        return ProjectSerializer(projects, many=True).data

    def get_activities(self, obj):

        activity = Activity.objects.filter(department=obj.id)
        return ActivitySerializer(activity, many=True).data

    def get_photos(self, obj):

        photo = DepartmentPhotos.objects.filter(department=obj.id)
        return DepartmentPhotosSerializer(photo, many=True).data

    def get_news(self, obj):

        news = DepartmentNews.objects.filter(department=obj.id)
        return DepartmentNewsSerializer(news, many=True).data

    hod = serializers.SerializerMethodField()
    people = serializers.SerializerMethodField()
    programmes = serializers.SerializerMethodField()
    facilities = serializers.SerializerMethodField()
    research = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()
    news = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('name', 'short_code', 'about_us', 'mission', 'vision', 'contact_us', 'hod', 'people', 'programmes', 'research', 'projects', 'activities', 'facilities', 'photos', 'news')
