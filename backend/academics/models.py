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
