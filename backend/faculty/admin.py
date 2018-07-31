from django.contrib import admin
from faculty.models import *
from department.models import Faculty

class GeneralInformationModelAdmin(admin.ModelAdmin):

    list_display = ['__str__', '_department', '_education', '_work_experience', '_projects']
    
    def get_queryset(self, request):
        queryset = super(GeneralInformationModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(GeneralInformationModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class BooksPatentsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_file', '_url']

    def get_queryset(self, request):
        queryset = super(BooksPatentsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(BooksPatentsModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class PublicationModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_authors', '_journal']

    def get_queryset(self, request):
        queryset = super(PublicationModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
             return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(PublicationModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class PublicationPDFModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_publication']

    def get_queryset(self, request):
        queryset = super(PublicationPDFModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
             return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(PublicationPDFModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ConferenceModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_authors', '_location']

    def get_queryset(self, request):
        queryset = super(ConferenceModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
             return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(ConferenceModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ConferencePDFModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_conference']

    def get_queryset(self, request):
        queryset = super(ConferencePDFModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
             return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(ConferencePDFModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_file']

    def get_queryset(self, request):
        queryset = super(StudentsModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty_id__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty_id':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
        return super(StudentsModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


admin.site.register(GeneralInformation, GeneralInformationModelAdmin)
admin.site.register(BooksPatents, BooksPatentsModelAdmin)
admin.site.register(Publication, PublicationModelAdmin)
admin.site.register(Conference, ConferenceModelAdmin)
admin.site.register(ConferencePDF, ConferencePDFModelAdmin)
admin.site.register(PublicationPDF, PublicationPDFModelAdmin)
admin.site.register(Students, StudentsModelAdmin)