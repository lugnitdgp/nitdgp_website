from django.contrib import admin
from academics.models import *


class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']


class CalendarModelAdmin(admin.ModelAdmin):
    list_display = ['_file', '_year']


admin.site.register(Notice, NoticeModelAdmin)
admin.site.register(Calendar, CalendarModelAdmin)
