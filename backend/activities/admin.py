from django.contrib import admin
from activities.models import *


class StudentClubModelAdmin(admin.ModelAdmin):
	list_display = ['_name', '_description', '_link']


class FestivalModelAdmin(admin.ModelAdmin):
	list_display = ['_name', '_description', '_link']


class GrievanceCellModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_url', '_date']


class SeminarEventModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'archive', 'date']
	search_fields = ['title', 'date']
	list_filter = ['date', 'archive']
	list_editable = ['archive', 'date']
	actions = ['archive_events', 'restore_events']

	def archive_events(self, request, queryset):
		queryset.update(archive=True)

	def restore_events(self, request, queryset):
		queryset.update(archive=False)


class AchievementModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date']


class ResearchModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date', '_url']


class PlacementModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date', '_url']


class PlacementLinksModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_date', '_url']

class CollaborationModelAdmin(admin.ModelAdmin):
	list_display = ['_title', '_file', '_type', '_date', '_url']

class BricsModelAdmin(admin.ModelAdmin):
	list_display = ['title', '_file', '_date']

class CoeModelAdmin(admin.ModelAdmin):
	list_display = ['_name', '_description', '_link']

class CoecarouselModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_type', '_secondary', '_image']


class VisitorModelAdmin(admin.ModelAdmin):
	list_display = ['_name', '_designation', '_event_name']


class OutreachModelAdmin(admin.ModelAdmin):
        list_display = ['category', 'name']

class NewsletterModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'date']

class CovidModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'date']

admin.site.register(Outreach, OutreachModelAdmin)
admin.site.register(StudentClub, StudentClubModelAdmin)
admin.site.register(Festival, FestivalModelAdmin)
admin.site.register(GrievanceCell, GrievanceCellModelAdmin)
admin.site.register(SeminarEvent, SeminarEventModelAdmin)
admin.site.register(Achievement, AchievementModelAdmin)
admin.site.register(Research, ResearchModelAdmin)
admin.site.register(Placement, PlacementModelAdmin)
admin.site.register(Collaboration, CollaborationModelAdmin)
admin.site.register(Brics, BricsModelAdmin)
admin.site.register(Coe, CoeModelAdmin)
admin.site.register(Coecarousel, CoecarouselModelAdmin)
admin.site.register(PlacementLinks, PlacementLinksModelAdmin)
admin.site.register(Visitor, VisitorModelAdmin)
admin.site.register(Newsletter, NewsletterModelAdmin)
admin.site.register(Covid, CovidModelAdmin)
