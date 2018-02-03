from rest_framework import serializers
from department.models import *
import collections


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'short_code',)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'short_code', 'about_us', 'mission', 'vision')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('name', 'research_interest', 'email', 'mobile', 'joining_year')


class OfferingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programme
        fields = ('degree',)
        depth = 1


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ('title', 'short_code', 'semester', 'course_type', 'credits',)


class PeopleSerializer(serializers.ModelSerializer):

    faculty = serializers.SerializerMethodField()

    def get_faculty(self, obj):
        result = collections.defaultdict()
        prof = Roles.objects.filter(name="Professor").first()
        associate_prof = Roles.objects.filter(name="Associate Professor").first()
        assistant_prof = Roles.objects.filter(name="Assistant Professor").first()
        for i in self.instance.all():
            for j in i.facultyroles_set.all():
                if j.role_id == associate_prof.id or j.role_id == prof.id or j.role_id == assistant_prof.id:
                    try:
                        result[j.role.name].append({
                            'details': FacultySerializer(Faculty.objects.filter(pk=i.id), many=True).data
                        })
                    except KeyError:
                        result[j.role.name] = [{
                            'details': FacultySerializer(Faculty.objects.filter(pk=i.id), many=True).data
                        }]
        return result

    class Meta:
        model = Faculty
        fields = ('faculty', )


class MainSerializer(serializers.ModelSerializer):

    offerings = serializers.SerializerMethodField()

    def get_offerings(self, obj):

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

    class Meta:
        model = Department
        fields = ('offerings',)


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'short_code', 'about_us', 'mission', 'vision')


class HodSerializer(serializers.ModelSerializer):

    department = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Faculty
        fields = ('id', 'name', 'research_interest', 'email', 'mobile', 'joining_year', 'department')
