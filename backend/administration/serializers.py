from rest_framework import serializers
from administration.models import *
from department.models import Roles, HOD
from department.serializers import FacultySerializer


class BOGSerializer(serializers.ModelSerializer):

    class Meta:
        model = BOG
        fields = ('name', 'designation', 'image', 'address', 'role')


class BwcIfcSerializer(serializers.ModelSerializer):

    class Meta:
        model = BwcIfc
        fields = ('title', 'file', 'date')


class SenateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Senate
        fields = ('title', 'file', 'date')


class BogAgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = BogAgenda
        fields = ('title', 'file', 'date')


class DeanSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField(source='faculty.id')
    name = serializers.ReadOnlyField(source='faculty.name')
    email = serializers.ReadOnlyField(source='faculty.email')
    mobile = serializers.ReadOnlyField(source='faculty.mobile')
    image = serializers.ImageField(source='faculty.image')
    department = serializers.ReadOnlyField(source='faculty.department.name')

    class Meta:
        model = Dean
        fields = ('id', 'name', 'role', 'designation', 'email', 'mobile', 'image', 'department')


class WardenSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField(source='faculty.id')
    name = serializers.ReadOnlyField(source='faculty.name')
    email = serializers.ReadOnlyField(source='faculty.email')
    mobile = serializers.ReadOnlyField(source='faculty.mobile')
    image = serializers.ImageField(source='faculty.image')
    department = serializers.ReadOnlyField(source='faculty.department.name')

    class Meta:
        model = Warden
        fields = ('id', 'name', 'role', 'designation', 'email', 'mobile', 'image', 'department')


class HODSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField(source='faculty.id')
    name = serializers.ReadOnlyField(source='faculty.name')
    email = serializers.ReadOnlyField(source='faculty.email')
    mobile = serializers.ReadOnlyField(source='faculty.mobile')
    research_interest = serializers.ReadOnlyField(source='faculty.research_interest')
    joining_year = serializers.ReadOnlyField(source='faculty.joining_year')
    image = serializers.ImageField(source='faculty.image')
    department = serializers.ReadOnlyField(source='department.name')
    department_shortcode = serializers.ReadOnlyField(source='department.short_code')

    class Meta:

        model = HOD
        fields = ('id', 'name', 'email', 'mobile', 'research_interest', 'joining_year', 'image', 'department', 'department_shortcode')


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ('name', 'designation', 'phone', 'email', 'photo')
