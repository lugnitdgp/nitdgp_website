from django.contrib import admin
from faculty.models import *

class GeneralInformationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_department', '_education', '_work_experience', '_projects']


admin.site.register(GeneralInformation, GeneralInformationModelAdmin)
