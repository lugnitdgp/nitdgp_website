from django.contrib import admin
from department.models import *

# Register your models here.


class FacultyModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department']


class ResearchModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_institute_involved', '_faculty_involved']


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_institute_involved', '_faculty_involved', '_funding']


class RolesModelAdmin(admin.ModelAdmin):
    list_display = ['__str__']


class FacultyRolesModelAdmin(admin.ModelAdmin):
    list_display = ['_faculty', '_role']


class ActivitiesModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_speakers', '_programme', '_date']


class DegreeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_description']


class ProgrammeModelAdmin(admin.ModelAdmin):
    list_display = ['_title', '_degree', '_department']


class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ['_programme', '_short_code', '_semester', '_course_type']


class FacilityModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_category']
    ordering = ('department', '-category', )


class ElectivesModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_title', '_is_open', '_semester']


class DepartmentPhotosModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_title', '_date']


class DepartmentNewsModelAdmin(admin.ModelAdmin):
    list_display = ['_department', '_title', '_date']


admin.site.register(Department)
admin.site.register(Faculty, FacultyModelAdmin)
admin.site.register(Research, ResearchModelAdmin)
admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Roles, RolesModelAdmin)
admin.site.register(FacultyRoles, FacultyRolesModelAdmin)
admin.site.register(Activity, ActivitiesModelAdmin)
admin.site.register(Degree, DegreeModelAdmin)
admin.site.register(Programme, ProgrammeModelAdmin)
admin.site.register(Courses, CoursesModelAdmin)
admin.site.register(Facility, FacilityModelAdmin)
admin.site.register(Electives, ElectivesModelAdmin)
admin.site.register(DepartmentNews, DepartmentNewsModelAdmin)
admin.site.register(DepartmentPhotos, DepartmentPhotosModelAdmin)
