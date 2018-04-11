from rest_framework import serializers
from administration.models import *
from department.models import *


class BOGSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='faculty.name')
    email = serializers.ReadOnlyField(source='faculty.email')
    mobile = serializers.ReadOnlyField(source='faculty.mobile')
    joining_year = serializers.ReadOnlyField(source='faculty.joining_year')

    class Meta:
        model = BOG
        fields = ('name', 'email', 'mobile', 'joining_year')


class BwcIfcSerializer(serializers.ModelSerializer):

    class Meta:
        model = BwcIfc
        fields = ('title', 'file', 'date')


class SenateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Senate
        fields = ('title', 'file', 'date')


class DeanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dean
        fields = ('name', 'image', 'designation', 'role', 'email', 'phone', 'alternate_phone')