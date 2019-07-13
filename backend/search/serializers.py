from rest_framework import serializers
from academics.models import Notice, HostelNotice
from department.models import Faculty


class GeneralNoticeSearchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=1024)
    notice_type = serializers.SerializerMethodField()
    file = serializers.FileField(required=False)
    date = serializers.DateField()

    def get_notice_type(self, obj):
        if isinstance(obj, HostelNotice):
            return 'Hostel'
        return getattr(obj, 'notice_type', None)


class FacultySearchSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Faculty
        fields = ('name', 'email', 'designation', 'department',
                  'mobile', 'joining_year', 'image')
