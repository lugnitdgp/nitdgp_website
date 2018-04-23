from django.contrib import admin
from faculty.models import *

class GeneralInformationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_education', '_work_experience', '_projects']


class BooksPatentsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_file', '_url']


class PublicationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_authors', '_journal']


class StudentsModelAdmin(admin.ModelAdmin):
	list_display = ['__str__', '_title', '_file']

admin.site.register(GeneralInformation, GeneralInformationModelAdmin)
admin.site.register(BooksPatents, BooksPatentsModelAdmin)
admin.site.register(Publication, PublicationModelAdmin)
admin.site.register(Students, StudentsModelAdmin)