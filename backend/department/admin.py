from django.contrib import admin
from department.models import *
from ckeditor.widgets import CKEditorWidget


class FacultyModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['name', 'department']

    def get_queryset(self, request):
        queryset = super(FacultyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        group = request.user.groups.first()
        if group.name=='Faculty':
            return queryset.filter(name=request.user.get_full_name())
        return queryset.filter(department__name=request.user.get_full_name())

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'department':
    #         if not request.user.is_superuser:
    #             kwargs["queryset"] = Department.objects.filter(
    #                 name=request.user.get_full_name())
    #     return super(FacultyModelAdmin, self).formfield_for_foreignkey(
    #         db_field, request, **kwargs)


class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_designation', '_department']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(StaffModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(StaffModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ResearchModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_institute_involved', '_faculty_involved', '_date']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(ResearchModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(ResearchModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_institute_involved', '_faculty_involved', '_funding', '_date']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(ProjectModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(ProjectModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class RolesModelAdmin(admin.ModelAdmin):
    list_display = ['__str__']



class FacultyRolesModelAdmin(admin.ModelAdmin):
    list_display = ['_faculty', '_department']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(FacultyRolesModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty__department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    department__name=request.user.get_full_name())
        return super(FacultyRolesModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class HODModelAdmin(admin.ModelAdmin):
    list_display = ['_faculty', '_department']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(HODModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty__department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    department__name=request.user.get_full_name())
        return super(HODModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ActivitiesModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_speakers', '_programme', '_start_date', '_end_date']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(ActivitiesModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(ActivitiesModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class DegreeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_description']


class ProgrammeModelAdmin(admin.ModelAdmin):
    list_display = ['_title', '_degree', '_department']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(ProgrammeModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(ProgrammeModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ['_programme', '_short_code', '_semester', '_l', '_t', '_s']

    def get_queryset(self, request):
        queryset = super(CoursesModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(programme__department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'programme':
            if not request.user.is_superuser:
                kwargs["queryset"] = Programme.objects.filter(
                    department__name=request.user.get_full_name())
        return super(CoursesModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class FacilityModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_category']
    ordering = ('department', '-category', )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(FacilityModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(FacilityModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ElectivesModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_title', '_is_open', '_semester']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(ElectivesModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(ElectivesModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

class DepartmentPhotosModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_title', '_date']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(DepartmentPhotosModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(DepartmentPhotosModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class DepartmentNewsModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_title', '_date']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(DepartmentNewsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(DepartmentNewsModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_file']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['department']

    def get_queryset(self, request):
        queryset = super(StudentModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(StudentModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class SyllabusModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_degree', '_department']

    def get_queryset(self, request):
        queryset = super(SyllabusModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(department__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            if not request.user.is_superuser:
                kwargs["queryset"] = Department.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Department.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(SyllabusModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


admin.site.register(Department)
admin.site.register(Faculty, FacultyModelAdmin)
admin.site.register(Staff, StaffModelAdmin)
admin.site.register(Student, StudentModelAdmin)
admin.site.register(Research, ResearchModelAdmin)
admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Roles, RolesModelAdmin)
admin.site.register(HOD, HODModelAdmin)
admin.site.register(FacultyRoles, FacultyRolesModelAdmin)
admin.site.register(Activity, ActivitiesModelAdmin)
admin.site.register(Degree, DegreeModelAdmin)
admin.site.register(Programme, ProgrammeModelAdmin)
admin.site.register(Courses, CoursesModelAdmin)
admin.site.register(Facility, FacilityModelAdmin)
admin.site.register(Electives, ElectivesModelAdmin)
admin.site.register(DepartmentNews, DepartmentNewsModelAdmin)
admin.site.register(DepartmentPhotos, DepartmentPhotosModelAdmin)
admin.site.register(Syllabus, SyllabusModelAdmin)
