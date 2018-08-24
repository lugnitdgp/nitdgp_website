from django.contrib import admin
from faculty.models import *
from department.models import Faculty


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


class EducationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_education']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(EducationModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class TeachingsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_teachings']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(TeachingsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class AwardsAndRecognitionModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_awards_and_recognition']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(AwardsAndRecognitionModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class ProjectsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_projects']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(ProjectsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class WorkExperienceModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_work_experience']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(WorkExperienceModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class AdministrativeResponsibilityModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_administrative_responsibilities']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(AdministrativeResponsibilityModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


admin.site.register(AdministrativeResponsibility, AdministrativeResponsibilityModelAdmin)
admin.site.register(WorkExperience, WorkExperienceModelAdmin)
admin.site.register(Projects, ProjectsModelAdmin)
admin.site.register(AwardsAndRecognition, AwardsAndRecognitionModelAdmin)
admin.site.register(Education, EducationModelAdmin)
admin.site.register(Teachings, TeachingsModelAdmin)
admin.site.register(Students, StudentsModelAdmin)
