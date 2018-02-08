from rest_framework import serializers
from administration.models import BOG


class BOGSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='faculty.name')
    email = serializers.ReadOnlyField(source='faculty.email')
    mobile = serializers.ReadOnlyField(source='faculty.mobile')
    joining_year = serializers.ReadOnlyField(source='faculty.joining_year')

    class Meta:
        model = BOG
        fields = ('name', 'email', 'mobile', 'joining_year')
