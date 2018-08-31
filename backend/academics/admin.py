from django.contrib import admin
from academics.models import *


class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_notice_type', '_file', '_date']


class AdmissionDegreeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_description']


class AdmissionProgrammeModelAdmin(admin.ModelAdmin):
    list_display = ['_degree', '__str__', '_description']


class AdmissionModelAdmin(admin.ModelAdmin):
    list_display = ['_programme', '_title', '_file', '_link']


class ExaminationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_year', '_file']


class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_type', '_filename']


class RegulationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class ConvocationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_url']


admin.site.register(Notice, NoticeModelAdmin)
admin.site.register(Calendar)
admin.site.register(Convocation, ConvocationModelAdmin)
admin.site.register(AdmissionDegree, AdmissionDegreeModelAdmin)
admin.site.register(AdmissionProgramme, AdmissionProgrammeModelAdmin)
admin.site.register(Admission, AdmissionModelAdmin)
admin.site.register(Examination, ExaminationModelAdmin)
admin.site.register(Document, DocumentModelAdmin)
admin.site.register(Regulation, RegulationModelAdmin)
admin.site.register(Registration, RegistrationModelAdmin)
