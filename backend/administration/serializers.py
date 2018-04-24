from rest_framework import serializers
from administration.models import *
from department.models import Roles, FacultyRoles
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

    class Meta:
        model = Dean
        fields = ('name', 'image', 'designation', 'role', 'email', 'phone', 'alternate_phone')


class HODSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='faculty.name')
    email = serializers.ReadOnlyField(source='faculty.email')
    mobile = serializers.ReadOnlyField(source='faculty.mobile')
    research_interest = serializers.ReadOnlyField(source='faculty.research_interest')
    joining_year = serializers.ReadOnlyField(source='faculty.joining_year')
    image = serializers.ImageField(source='faculty.image')
    department = serializers.ReadOnlyField(source='faculty.department.name')

    class Meta:

        model = FacultyRoles
        fields = ('name', 'email', 'mobile', 'research_interest', 'joining_year', 'image', 'department')
