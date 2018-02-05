from django.contrib import admin
from administration.models import *


class BOGModelAdmin(admin.ModelAdmin):
    list_display = ['_role', '_name']

# Register your models here.


admin.site.register(BOG, BOGModelAdmin)
