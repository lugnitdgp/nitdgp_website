import datetime
from django.core.validators import validate_integer
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

     CATEGORY_CHOICES = (('SCI','SCI'),('SCIE','SCIE'),('ESCI','ESCI'),('SCOPUS','SCOPUS'),('Web of Science','Web of Science'),('Others','Others'))
     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
     authors = models.CharField(max_length=300, default='')
     title = RichTextField()
     journal = models.TextField()
     vol_or_page = models.CharField(max_length=200)
     publisher = models.CharField(max_length=300, default='')
     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='SCI/SCOPUS')
     doi = models.CharField(max_length=200, blank=True)
     year = models.CharField(max_length=100, validators=[validate_integer])

     def __str__(self):
         return self.faculty.name

     def _title(self):
        return self.title

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

    YEAR_CHOICES = [(r, r) for r in range((datetime.date.today().year),1959,-1)]
    PATENT_STATUS = (('Submitted','Submitted'),('Granted','Granted'))
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = RichTextField()
    patent_inventor = models.CharField(max_length=512, default='')
    patent_filed_year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=1959
    )
    patent_Granted_year = models.CharField(
        max_length=512,
        choices=YEAR_CHOICES,
        default=''
    )
    patent_status = models.CharField(max_length=100, choices=PATENT_STATUS, default='Submitted')
    link = models.CharField(max_length=512, blank=True)
    file = models.FileField(upload_to=rename_patents, blank=True)
    

    def __str__(self):
        return self.faculty.name

    def _title(self):
        return self.title

    def _file(self):
        return self.file
