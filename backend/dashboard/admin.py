from django.contrib import admin
from dashboard.models import Section, Tile


class SectionModelManager(admin.ModelAdmin):
    list_display = ['__str__', '_priority', '_tiles']


class TileModelManager(admin.ModelAdmin):
    list_display = ['__str__', '_section', '_row', '_column']

# Register your models here.


admin.site.register(Section, SectionModelManager)
admin.site.register(Tile, TileModelManager)
