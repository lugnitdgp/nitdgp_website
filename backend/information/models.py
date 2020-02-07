from django.db import models
from base.models import BaseModel


class Report(BaseModel):

    class Meta:
        ordering = ('-created_at', )

    CHOICES = (('Annual', 'Annual'), ('Audit', 'Audit'))
    title = models.CharField(max_length=255)
    type = models.CharField(choices=CHOICES, max_length=255)
    file = models.FileField(upload_to='information/reports/%Y')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _type(self):
        return self.type


class Account(BaseModel):

    class Meta:
        ordering = ('-created_at', )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/accounts/%Y')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class Career(BaseModel):

    class Meta:
        ordering = ('-created_at', )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/careers/%Y', blank=True)
    link = models.URLField(blank=True)
    archive = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class Tender(BaseModel):

    class Meta:
        ordering = ('-created_at', )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/tender/%Y')
    archive = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class TEQIP(BaseModel):

    class Meta:
        verbose_name_plural = 'TEQIP'
        ordering = ('-created_at', )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/teqip/%Y')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class RTI(BaseModel):

    class Meta:
        verbose_name_plural = 'RTI'
        ordering = ('-created_at', )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/rti/%Y', blank=True)
    link = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

class ReplyRTI(BaseModel):
    class meta:
        verbose_name_plural = 'ReplyRTI'
        ordering = ('-request_date',)

    request_no = models.CharField(max_length=250)
    request = models.FileField(upload_to='information/rti_request/%Y')
    request_date = models.DateField()
    reply = models.FileField(upload_to='information/rti_reply/%Y')
    reply_date = models.DateField()

    def __str__(self):
        return self.request_no

    def _request(self):
        return self.request
    
    def _reply(self):
        return self.reply

    def _request_date(self):
        return self.request_date

    def _reply_date(self):
        return self.reply_date

class NIRF(BaseModel):

    class Meta:
        verbose_name_plural = 'NIRF'
        ordering = ('-created_at', )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/nirf/%Y')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class NBA(BaseModel):

    class Meta:
        verbose_name_plural = 'NBA'
        ordering = ('-created_at', )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/nba/%Y')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class OfficeNotice(BaseModel):

    class Meta:
        verbose_name_plural = 'Office Notices'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/officenotice/%Y')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _date(self):
        return self.date


class More(BaseModel):

    class Meta:
        verbose_name_plural = 'More Information'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/more/%Y', blank=True)
    link = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _date(self):
        return self.date


class PublicGrievance(BaseModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/public_grievance/%Y', blank=True)
    link = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title


class ICC(BaseModel):
    class Meta:
        verbose_name_plural = 'ICC'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/ICC/%Y', blank=True)
    link = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class NAD(BaseModel):
    class Meta:
        verbose_name_plural = 'National Academic Depository'

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/NAD/%Y', blank=True)
    link = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class Promotion(BaseModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='information/Promotion/%Y')
    
    def __str__(self):
        return self.title
