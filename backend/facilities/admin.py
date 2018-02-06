from django.contrib import admin
from facilities.models import *


class LibraryModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_home', '_about', '_contact_us']


class E_resourcesModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_url']


admin.site.register(Library, LibraryModelAdmin)
admin.site.register(E_resource, E_resourcesModelAdmin)
