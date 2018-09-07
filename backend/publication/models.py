from django.db import models
from base.models import BaseModel
from ckeditor.fields import RichTextField
from department.models import Faculty


class Conference(BaseModel):

     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
     citation = RichTextField()
     location = models.TextField(blank=True)
     year = models.CharField(max_length=100, blank=True)

     def __str__(self):
         return self.faculty.name

     def _citation(self):
        return self.citation

     def _location(self):
        return self.location

     def _year(self):
        return self.year


class Journal(BaseModel):

     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
     citation = RichTextField()
     journal = models.TextField(blank=True)
     year = models.CharField(max_length=100, blank=True)

     def __str__(self):
         return self.faculty.name

     def _citation(self):
        return self.citation

     def _journal(self):
        return self.journal

     def _year(self):
        return self.year


def rename_book(instance, filename):

    return 'faculty/{0}/books_and_book_chapters/{1}'.format(instance.faculty.name, filename)


class Book(BaseModel):

    class Meta:
        verbose_name_plural = 'Books and Book Chapters'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = RichTextField()
    file = models.FileField(upload_to=rename_book, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.faculty.name

    def _title(self):
        return self.title

    def _file(self):
        return self.file

    def _url(self):
        return self.url


def rename_patents(instance, filename):

    return 'faculty/{0}/Patents/{1}'.format(instance.faculty.name, filename)


class Patent(BaseModel):

    class Meta:
        verbose_name_plural = 'Patents'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = RichTextField()
    file = models.FileField(upload_to=rename_patents, blank=True)

    def __str__(self):
        return self.faculty.name

    def _title(self):
        return self.title

    def _file(self):
        return self.file
