from django.contrib import admin
from activities.models import *


class StudentClubModelAdmin(admin.ModelAdmin):
	list_display = ['_name', '_description', '_link']


class SeminarEventModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date']


class AchievementModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date']

admin.site.register(StudentClub, StudentClubModelAdmin)
admin.site.register(SeminarEvent, SeminarEventModelAdmin)
admin.site.register(Achievement, AchievementModelAdmin)