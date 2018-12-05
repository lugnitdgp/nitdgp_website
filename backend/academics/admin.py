from django.contrib import admin
from academics.models import *


class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'archive', 'notice_type', 'date']
    list_editable = ['notice_type', 'archive']
    list_filter = ['notice_type', 'archive', 'date']
    search_fields = ['title', 'date']
    actions = ['archive_notices', 'restore_notices']

    def archive_notices(self, request, queryset):
        queryset.update(archive=True)

    def restore_notices(self, request, queryset):
        queryset.update(archive=False)

    def get_queryset(self, request):
        queryset = super(NoticeModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        groups = request.user.groups.filter(name__endswith=" Notice")
        notice_types = [x.name.split()[0] for x in groups]
        return queryset.filter(notice_type__in=notice_types)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "notice_type" and not request.user.is_superuser:
            groups = request.user.groups.filter(name__endswith=" Notice")
            kwargs['choices'] = (
                (x.name.split()[0], x.name.split()[0]) for x in groups
            )
        return super().formfield_for_choice_field(db_field, request, **kwargs)


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


class FeeModelAdmin(admin.ModelAdmin):
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
admin.site.register(Fee, FeeModelAdmin)
admin.site.register(Registration, RegistrationModelAdmin)
