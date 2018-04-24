from django.contrib import admin
from administration.models import *

class DeanModelAdmin(admin.ModelAdmin):
	list_display = ['__str__', '_image', '_designation', '_role', '_email', '_phone']


class BOGModelAdmin(admin.ModelAdmin):
    list_display = ['_role', '_name', '_designation', '_address']


class BwcIfcModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_type', '_date']

class SenateAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']

class BogAgendaAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']

# Register your models here.

admin.site.register(Dean, DeanModelAdmin)
admin.site.register(BOG, BOGModelAdmin)
admin.site.register(BwcIfc, BwcIfcModelAdmin)
admin.site.register(Senate, SenateAdmin)
admin.site.register(BogAgenda, BogAgendaAdmin)
