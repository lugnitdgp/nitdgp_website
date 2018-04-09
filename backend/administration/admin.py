from django.contrib import admin
from administration.models import *


class BOGModelAdmin(admin.ModelAdmin):
    list_display = ['_role', '_name']


class BwcIfcModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_type', '_date']

# Register your models here.


admin.site.register(BOG, BOGModelAdmin)
admin.site.register(BwcIfc, BwcIfcModelAdmin)
