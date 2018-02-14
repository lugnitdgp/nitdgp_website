from django.contrib import admin
from facilities.models import *
from ckeditor.widgets import CKEditorWidget


class LibraryModelAdmin(admin.ModelAdmin):
    list_display = ['_home', '_about', '_contact_us']


class EResourceModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_url']

class SACModelAdmin(admin.ModelAdmin):
	list_display = ['_about','__str__','_other_activities','_facility','_contact_us','_ach_url','_rec_url']

class CIFModelAdmin(admin.ModelAdmin):
	list_display = ['_equipment_name','_equipment_desc']


admin.site.register(Library, LibraryModelAdmin)
admin.site.register(EResource, EResourceModelAdmin)
admin.site.register(SAC,SACModelAdmin)
admin.site.register(CIF,CIFModelAdmin)
