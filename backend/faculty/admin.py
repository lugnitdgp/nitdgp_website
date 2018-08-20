from django.contrib import admin
from faculty.models import *
from department.models import Faculty

class GeneralInformationModelAdmin(admin.ModelAdmin):

    list_display = ['__str__', '_department', '_education', '_work_experience', '_projects']

    def get_queryset(self, request):
        queryset = super(GeneralInformationModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(GeneralInformationModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_file']

    def get_queryset(self, request):
        queryset = super(StudentsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(StudentsModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


admin.site.register(GeneralInformation, GeneralInformationModelAdmin)
admin.site.register(Students, StudentsModelAdmin)
