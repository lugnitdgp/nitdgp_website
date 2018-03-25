from django.db import models
from base.models import BaseModel


class Report(BaseModel):
    CHOICES = (('Annual', 'Annual'), ('Audit', 'Audit'))
    title = models.CharField(max_length=255)
    type = models.CharField(choices=CHOICES, max_length=255)
    file = models.FileField(upload_to='information/reports/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _type(self):
        return self.type


class Account(BaseModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/accounts/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class Career(BaseModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/careers/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class Tender(BaseModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/tender/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class TEQIP(BaseModel):

    class Meta:
        verbose_name_plural = 'TEQIP'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/teqip/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class RTI(BaseModel):

    class Meta:
        verbose_name_plural = 'RTI'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/rti/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class NIRF(BaseModel):

    class Meta:
        verbose_name_plural = 'NIRF'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/nirf/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class NBA(BaseModel):

    class Meta:
        verbose_name_plural = 'NBA'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/nba/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file
