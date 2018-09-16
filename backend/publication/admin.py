from django.contrib import admin
from publication.models import *
from department.models import Faculty

class BookModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_file', '_url']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(BookModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(BookModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class JournalModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_citation', '_year', '_journal']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(JournalModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
             return queryset
        return queryset.filter(faculty__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(JournalModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class ConferenceModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_citation', '_year', '_location']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(ConferenceModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
             return queryset
        return queryset.filter(faculty__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(ConferenceModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class PatentModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_title', '_file']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj is None:
            return []
        return ['faculty']

    def get_queryset(self, request):
        queryset = super(PatentModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(faculty__name=request.user.get_full_name())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'faculty':
            if not request.user.is_superuser:
                kwargs["queryset"] = Faculty.objects.filter(
                    name=request.user.get_full_name())
                kwargs["initial"] = Faculty.objects.filter(
                    name=request.user.get_full_name()).first()
        return super(PatentModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


admin.site.register(Book, BookModelAdmin)
admin.site.register(Journal, JournalModelAdmin)
admin.site.register(Conference, ConferenceModelAdmin)
admin.site.register(Patent, PatentModelAdmin)
