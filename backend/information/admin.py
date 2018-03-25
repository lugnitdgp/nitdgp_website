from django.contrib import admin
from information.models import *


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_type']


class AccountModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class CareerModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class TenderModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class TEQIPModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class RTIModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class NIRFModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class NBAModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


admin.site.register(Report, ReportModelAdmin)
admin.site.register(Account, AccountModelAdmin)
admin.site.register(Career, CareerModelAdmin)
admin.site.register(Tender, TenderModelAdmin)
admin.site.register(TEQIP, TEQIPModelAdmin)
admin.site.register(RTI, RTIModelAdmin)
admin.site.register(NIRF, NIRFModelAdmin)
admin.site.register(NBA, NBAModelAdmin)
