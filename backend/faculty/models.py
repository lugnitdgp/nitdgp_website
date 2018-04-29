from django.db import models
from base.models import BaseModel
from ckeditor.fields import RichTextField
from department.models import Faculty, Courses

class GeneralInformation(BaseModel):

    class Meta:
        verbose_name_plural = 'General Information'

    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    education = RichTextField()
    work_experience = RichTextField()
    projects = RichTextField()
    awards_and_recognition = RichTextField()
    administrative_responsibilities = RichTextField()
    teachings = models.ManyToManyField(Courses)

    def __str__(self):
        return self.faculty_id.name

    def _department(self):
        return self.faculty_id.department.name

    def _education(self):
        return self.education

    def _work_experience(self):
        return self.work_experience

    def _projects(self):
        return self.projects

    def _teachings(self):
        return self.teachings


class Publication(BaseModel):

     faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
     authors = models.TextField()
     title = RichTextField()
     journal = models.TextField()
     year_or_volume = models.CharField(max_length=100)

     def __str__(self):
         return self.faculty_id.name

     def _title(self):
        return self.title

     def _authors(self):
        return self.authors

     def _journal(self):
        return self.journal


def rename_book(instance, filename):

    return 'faculty/{0}/books_and_patents/{1}'.format(instance.faculty_id.name, filename)


class BooksPatents(BaseModel):

    class Meta:
        verbose_name_plural = 'Books and Patents'

    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to=rename_book, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.faculty_id.name

    def _title(self):
        return self.title

    def _file(self):
        return self.file

    def _url(self):
        return self.url


def rename_students(instance, filename):

    return 'faculty/{0}/students/{1}'.format(instance.faculty_id.name, filename)


class Students(BaseModel):

    class Meta:
        verbose_name_plural = 'Students under Faculty'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to=rename_students)

    def __str__(self):
        return self.faculty_id.name

    def _title(self):
        return self.title

    def _file(self):
        return self.file