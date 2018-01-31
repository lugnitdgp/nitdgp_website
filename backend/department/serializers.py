from rest_framework import serializers
from department.models import Departments


class DepartmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = ('name', 'short_code')
