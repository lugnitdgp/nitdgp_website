from django.contrib import admin
from department.models import *

# Register your models here.

class FacultyModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department']

class ResearchModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_institute_involved', '_faculty_involved']

admin.site.register(Department)
admin.site.register(Faculty, FacultyModelAdmin)
admin.site.register(Research, ResearchModelAdmin)
