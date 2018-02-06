from django.contrib import admin
from academics.models import *


class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_link', '_date']


admin.site.register(Notice, NoticeModelAdmin)
