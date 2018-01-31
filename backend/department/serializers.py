from rest_framework import serializers
from department.models import Department


class DepartmentListSerializer(serializers.ModelSerializer):

    class Meta:
<<<<<<< HEAD
        model = Department
        fields = ('id', 'name', 'short_code')
=======
        model = Departments
        fields = ('name', 'short_code')
>>>>>>> fbb966b761fdbeac4ab1bf43cb03efa631dbb830
