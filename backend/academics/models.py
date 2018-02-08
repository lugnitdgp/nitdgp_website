from django.db import models
from base.models import BaseModel
import datetime

# Create your models here.


class Notice(BaseModel):
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='notices/%Y/%m/%d')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _date(self):
        return self.date


class Calendar(BaseModel):
    YEAR_CHOICES = [(str(r)+'-'+str(r+1), str(r)+'-'+str(r+1)) for r in range(1965, datetime.date.today().year+1)]
    year = models.CharField(max_length=20, choices=YEAR_CHOICES, default=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().year + 1))
    file = models.FileField(upload_to='calendar/%Y')

    def _file(self):
        return self.file

    def _year(self):
        return self.year


class AdmissionDegree(BaseModel):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def _description(self):
        return self.description


class AdmissionProgramme(BaseModel):
    degree = models.ForeignKey(AdmissionDegree, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    def _degree(self):
        return self.degree.name

    def __str__(self):
        return self.name

    def _description(self):
        return self.description


def rename_admission_file(instance, filename):

    return 'academics/admission/{0}/{1}/{2}'.format(instance.programme.degree.name, instance.programme.name, filename)


class Admission(BaseModel):
    programme = models.ForeignKey(AdmissionProgramme, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=rename_admission_file)

    def _programme(self):
        return self.programme.name

    def _title(self):
        return self.title

    def _file(self):
        return self.file
