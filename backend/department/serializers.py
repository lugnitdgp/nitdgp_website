from rest_framework import serializers
from department.models import Department


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'short_code')
