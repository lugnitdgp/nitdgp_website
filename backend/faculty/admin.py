from django.contrib import admin
from faculty.models import *
from department.models import Faculty


class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_name', '_degree', 'type']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(StudentsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(StudentsModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class EducationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_education']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        num_objects = self.model.objects.filter(faculty__name=request.user.get_full_name()).count()
        if num_objects >= 1:
          return False
        else:
          return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(EducationModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(EducationModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class TeachingsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_teachings']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        num_objects = self.model.objects.filter(faculty__name=request.user.get_full_name()).count()
        if num_objects >= 1:
          return False
        else:
          return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(TeachingsModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(TeachingsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class AwardsAndRecognitionModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_awards_and_recognition']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        num_objects = self.model.objects.filter(faculty__name=request.user.get_full_name()).count()
        if num_objects >= 1:
          return False
        else:
          return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(AwardsAndRecognitionModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(AwardsAndRecognitionModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class ProjectsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_projects']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        num_objects = self.model.objects.filter(faculty__name=request.user.get_full_name()).count()
        if num_objects >= 1:
          return False
        else:
          return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(ProjectsModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(ProjectsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class WorkExperienceModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_work_experience']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        num_objects = self.model.objects.filter(faculty__name=request.user.get_full_name()).count()
        if num_objects >= 1:
          return False
        else:
          return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(WorkExperienceModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(WorkExperienceModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class AdministrativeResponsibilityModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_administrative_responsibilities']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        num_objects = self.model.objects.filter(faculty__name=request.user.get_full_name()).count()
        if num_objects >= 1:
          return False
        else:
          return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(AdministrativeResponsibilityModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(AdministrativeResponsibilityModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class MiscModelAdmin(admin.ModelAdmin):
    list_display = ['__str__',]

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        num_objects = self.model.objects.filter(faculty__name=request.user.get_full_name()).count()
        if num_objects >= 1:
          return False
        else:
          return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(MiscModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(MiscModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())


class NotesModelAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'subject_name','semester', 'degree', 'secret_key']
    list_editable = ['secret_key']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(NotesModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(NotesModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())



admin.site.register(Notes, NotesModelAdmin)
admin.site.register(AdministrativeResponsibility, AdministrativeResponsibilityModelAdmin)
admin.site.register(WorkExperience, WorkExperienceModelAdmin)
admin.site.register(Projects, ProjectsModelAdmin)
admin.site.register(AwardsAndRecognition, AwardsAndRecognitionModelAdmin)
admin.site.register(Education, EducationModelAdmin)
admin.site.register(Teachings, TeachingsModelAdmin)
admin.site.register(Students, StudentsModelAdmin)
admin.site.register(Misc, MiscModelAdmin)
