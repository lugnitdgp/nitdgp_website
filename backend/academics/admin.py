from django.contrib import admin
from academics.models import *

def archive_selected(modeladmin, request, queryset):
    queryset.update(archive=True)
archive_selected.short_description = "Archive selected items"

def unarchive_selected(modeladmin, request, queryset):
    queryset.update(archive=False)
unarchive_selected.short_description = "Unarchive selected items"

class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'archive', 'notice_type', 'date']
    list_editable = ['notice_type', 'archive']
    list_filter = ['notice_type', 'archive', 'date']
    search_fields = ['title', 'date']
    actions = [archive_selected, unarchive_selected]

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

class NewAdmissionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', 'date']

class HostelNoticeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'archive', 'hall_type', 'date']
    list_editable = ['hall_type', 'archive']
    list_filter = ['hall_type', 'archive', 'date']
    search_fields = ['title', 'date']
    actions = [archive_selected, unarchive_selected]

    def get_queryset(self, request):
        queryset = super(HostelNoticeModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        groups = request.user.groups.filter(name__startswith="Hall")
        hall_types = [x.name.split()[1] for x in groups]
        return queryset.filter(hall_type__in=hall_types)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "hall_type" and not request.user.is_superuser:
            groups = request.user.groups.filter(name__startswith="Hall")
            kwargs['choices'] = (
                (x.name.split()[1], x.name.split()[1]) for x in groups
            )
        return super().formfield_for_choice_field(db_field, request, **kwargs)


class AdmissionDegreeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_description']


class AdmissionProgrammeModelAdmin(admin.ModelAdmin):
    list_display = ['_degree', '__str__', '_description']


class AdmissionModelAdmin(admin.ModelAdmin):
    list_display = ['_programme', '_title', '_file', '_link', 'archive']
    list_editable = ['archive']
    actions = [archive_selected, unarchive_selected]


class ExaminationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_year', '_file']


class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_type', '_filename']


class RegulationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class FeeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class CurriculumModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class ConvocationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', 'archive', '_url']
    actions = [archive_selected, unarchive_selected]

admin.site.register(Notice, NoticeModelAdmin)
admin.site.register(NewAdmission, NewAdmissionModelAdmin)
admin.site.register(HostelNotice, HostelNoticeModelAdmin)
admin.site.register(Calendar)
admin.site.register(Convocation, ConvocationModelAdmin)
admin.site.register(AdmissionDegree, AdmissionDegreeModelAdmin)
admin.site.register(AdmissionProgramme, AdmissionProgrammeModelAdmin)
admin.site.register(Admission, AdmissionModelAdmin)
admin.site.register(Examination, ExaminationModelAdmin)
admin.site.register(Document, DocumentModelAdmin)
admin.site.register(Regulation, RegulationModelAdmin)
admin.site.register(Fee, FeeModelAdmin)
admin.site.register(Curriculum, CurriculumModelAdmin)
admin.site.register(Registration, RegistrationModelAdmin)
