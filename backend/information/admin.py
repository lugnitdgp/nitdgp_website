from django.contrib import admin
from information.models import *


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_type']


class AccountModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class CareerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'archive', 'date']
    search_fields = ['title', 'date']
    list_filter = ['date', 'archive']
    list_editable = ['archive', 'date']
    actions = ['archive_careers', 'restore_careers']

    def archive_careers(self, request, queryset):
        queryset.update(archive=True)

    def restore_careers(self, request, queryset):
        queryset.update(archive=False)


class TenderModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'archive', 'date']
    search_fields = ['title', 'date']
    list_filter = ['date', 'archive']
    list_editable = ['archive', 'date']
    actions = ['archive_tenders', 'restore_tenders']

    def archive_tenders(self, request, queryset):
        queryset.update(archive=True)

    def restore_tenders(self, request, queryset):
        queryset.update(archive=False)


class TEQIPModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class RTIModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class NIRFModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class NBAModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class OfficeNoticeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']


class MoreModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']


admin.site.register(Report, ReportModelAdmin)
admin.site.register(Account, AccountModelAdmin)
admin.site.register(Career, CareerModelAdmin)
admin.site.register(Tender, TenderModelAdmin)
admin.site.register(TEQIP, TEQIPModelAdmin)
admin.site.register(RTI, RTIModelAdmin)
admin.site.register(NIRF, NIRFModelAdmin)
admin.site.register(NBA, NBAModelAdmin)
admin.site.register(OfficeNotice, OfficeNoticeModelAdmin)
admin.site.register(More, MoreModelAdmin)
admin.site.register(PublicGrievance)
admin.site.register(ICC)
admin.site.register(NAD)
