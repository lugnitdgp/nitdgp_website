from django.contrib import admin
from dashboard.models import *


class SectionModelManager(admin.ModelAdmin):
    list_display = ['__str__', '_priority', '_tiles']


class TileModelManager(admin.ModelAdmin):
    list_display = ['__str__', '_section', '_row', '_column']


class CarouselModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_secondary', '_image']


class EventModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']


class NewsFeedModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file', '_date']


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['_name', '_designation', '_group', '_contact']


admin.site.register(QuickLinks)
admin.site.register(Downloads)
admin.site.register(Section, SectionModelManager)
admin.site.register(Tile, TileModelManager)
admin.site.register(Carousel, CarouselModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(NewsFeed, NewsFeedModelAdmin)
admin.site.register(Contact, ContactModelAdmin)
