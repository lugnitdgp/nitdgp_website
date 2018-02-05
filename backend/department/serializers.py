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
        hods = Faculty.objects.filter(
            pk=FacultyRoles.objects.filter(role=hod_role).values_list('faculty')
        )
        department_hod = hods.filter(department=obj.id).first()
        return FacultySerializer(department_hod).data

    def get_people(self, obj):
        faculty = Faculty.objects.filter(department=obj.id)
        return PeopleSerializer(faculty, context=obj).data

    def get_programmes(self, obj):

        result = collections.defaultdict()
        for i in self.instance.programme_set.all():
            try:
                result[i.degree.name].append({
                    'programme_title': i.title,
                    'courses': CourseSerializer(i.courses_set.order_by('semester'), many=True).data
                })
            except KeyError:
                result[i.degree.name] = [{
                    'programme_title': i.title,
                    'courses': CourseSerializer(i.courses_set.order_by('semester'), many=True).data
                }]
        return result

    def get_facilities(self, obj):
        facilities = {'laboratory': [], 'equipment': []}
        departmental_facilities = Facility.objects.filter(department=obj.id)
        for facility in departmental_facilities:
            if facility.category == 'L':
                facilities['laboratory'].append(facility.name)
            else:
                facilities['equipment'].append(facility.name)

        return facilities

    hod = serializers.SerializerMethodField()
    people = serializers.SerializerMethodField()
    programmes = serializers.SerializerMethodField()
    facilities = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('name', 'short_code', 'about_us', 'mission', 'vision', 'hod', 'people', 'programmes', 'facilities')
