from django.contrib import admin
from activities.models import *


class StudentClubModelAdmin(admin.ModelAdmin):
	list_display = ['_name', '_description', '_link']


class SeminarEventModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_url', '_date']


class AchievementModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date']


class ResearchModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date', '_url']


class PlacementModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date', '_url']


class PlacementLinksModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date', '_url']


class VisitorModelAdmin(admin.ModelAdmin):
	list_display = ['_name', '_designation', '_event_name']


admin.site.register(StudentClub, StudentClubModelAdmin)
admin.site.register(SeminarEvent, SeminarEventModelAdmin)
admin.site.register(Achievement, AchievementModelAdmin)
admin.site.register(Research, ResearchModelAdmin)
admin.site.register(Placement, PlacementModelAdmin)
admin.site.register(PlacementLinks, PlacementLinksModelAdmin)
admin.site.register(Visitor, VisitorModelAdmin)
