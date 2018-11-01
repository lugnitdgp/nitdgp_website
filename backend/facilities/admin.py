from django.contrib import admin
from facilities.models import *
from ckeditor.widgets import CKEditorWidget


class LibraryModelAdmin(admin.ModelAdmin):
    list_display = ['_home', '_about', '_contact_us']

class ResourceModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_url', '_type']

class SACModelAdmin(admin.ModelAdmin):
	list_display = ['_about','__str__','_other_activities','_facility','_contact_us','_ach_url','_rec_url']

class HostelModelAdmin(admin.ModelAdmin):
    list_display = ['_name', ]

class CenterModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_description', '_link']

class CIFModelAdmin(admin.ModelAdmin):
	list_display = ['_equipment_name','_equipment_desc']

class SemesterquestionModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_file']
    
admin.site.register(Semesterquestion,SemesterquestionModelAdmin)
admin.site.register(Center, CenterModelAdmin)
admin.site.register(Library, LibraryModelAdmin)
admin.site.register(Resource, ResourceModelAdmin)
admin.site.register(SAC,SACModelAdmin)
admin.site.register(Hostel, HostelModelAdmin)
admin.site.register(CIF,CIFModelAdmin)
