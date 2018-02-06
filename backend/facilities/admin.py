from django.contrib import admin
from facilities.models import *


class LibraryModelAdmin(admin.ModelAdmin):
    list_display = ['_home', '_about', '_contact_us']


class EResourceModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_url']


admin.site.register(Library, LibraryModelAdmin)
admin.site.register(EResource, EResourceModelAdmin)
