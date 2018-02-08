from django.contrib import admin
from academics.models import *


class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']


class CalendarModelAdmin(admin.ModelAdmin):
    list_display = ['_file', '_year']


class AdmissionDegreeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_description']


class AdmissionProgrammeModelAdmin(admin.ModelAdmin):
    list_display = ['_degree', '__str__', '_description']


class AdmissionModelAdmin(admin.ModelAdmin):
    list_display = ['_programme', '_title', '_file']


admin.site.register(Notice, NoticeModelAdmin)
admin.site.register(Calendar, CalendarModelAdmin)
admin.site.register(AdmissionDegree, AdmissionDegreeModelAdmin)
admin.site.register(AdmissionProgramme, AdmissionProgrammeModelAdmin)
admin.site.register(Admission, AdmissionModelAdmin)
