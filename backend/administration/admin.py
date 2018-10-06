from django.contrib import admin
from administration.models import *


class DeanModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_image', '_designation', '_role', '_email']


class WardenModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_image', '_designation', '_role', '_email']


class BOGModelAdmin(admin.ModelAdmin):
    list_display = ['_role', '_name', '_designation', '_address']


class BwcIfcModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_type', '_date']


class SenateAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']


class BogAgendaAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']


class OfficerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'phone', 'mobile', 'email']


admin.site.register(Dean, DeanModelAdmin)
admin.site.register(BOG, BOGModelAdmin)
admin.site.register(BwcIfc, BwcIfcModelAdmin)
admin.site.register(Senate, SenateAdmin)
admin.site.register(Warden, WardenModelAdmin)
admin.site.register(BogAgenda, BogAgendaAdmin)
admin.site.register(Officer, OfficerModelAdmin)
