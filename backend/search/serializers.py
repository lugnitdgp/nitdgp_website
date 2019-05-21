from rest_framework import serializers
from academics.models import Notice
from department.models import Faculty


class NoticeSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title', 'notice_type', 'file', 'date')


class FacultySearchSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Faculty
        fields = ('name', 'email', 'designation', 'department',
                  'mobile', 'joining_year', 'image')
