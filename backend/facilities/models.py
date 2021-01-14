from django.db import models
from base.models import BaseModel
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator


class Center(BaseModel):

    title = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='dashboard/centers/')
    link = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def _description(self):
        return self.description

    def _link(self):
        return self.link


class Library(BaseModel):

    class Meta:
        verbose_name_plural = 'Library'

    home = RichTextField()
    about = RichTextField()
    contact_us = RichTextField()

    def _home(self):
        return self.home

    def _about(self):
        return self.about

    def _contact_us(self):
        return self.contact_us


class Resource(BaseModel):

    class Meta:
        verbose_name_plural = 'Resources'

    TYPES = (('E Resource', 'E Resource'), ('Text Resource', 'Text Resource'), ('eSoch Sindhu','eSoch Sindhu'),('Sodh Suddhi Access','Sodh Suddhi Access'),('NDLI e-Resources','NDLI e-Resources'))
    title = models.CharField(max_length=255, default="")
    url = models.URLField()
    type = models.CharField(choices=TYPES, max_length=512)

    def __str__(self):
        return self.title

    def _url(self):
        return self.url

    def _type(self):
        return self.type

class Semesterquestion(BaseModel):

    class Meta:
        verbose_name_plural = 'Semester Question'

    title = models.CharField(max_length=255, default="")
    file = models.FileField(upload_to='facilities/questions/%Y')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

class MedicalBulletin(BaseModel):
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='facilities/MU/%Y')
    link = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _date(self):
        return self.date

class SAC(BaseModel):

    class Meta:
        verbose_name_plural = 'Student Activity Center'

    about = RichTextField()
    mission = RichTextField()
    vision = RichTextField()
    program_offered = RichTextField()
    other_activities = RichTextField()
    facility = RichTextField()
    contact_us = RichTextField()
    image = models.FileField(upload_to='sac/images/%Y', blank=True)
    ach_url = models.URLField()
    rec_url = models.URLField()

    def _about(self):
        return self.about

    def __str__(self):
        return self.mission

    def __str__(self):
        return self.vision

    def __str__(self):
        return self.program_offered

    def _other_activities(self):
        return self.other_activities

    def _facility(self):
        return self.facility

    def _contact_us(self):
        return self.contact_us

    def _ach_url(self):
        return self.ach_url

    def _rec_url(self):
        return self.rec_url


def rename_image_cif_photo(instance,filename):

    return 'CIF/{0}/image/{1}'.format(instance.equipment_name,filename)


class Hostel(BaseModel):

    name = models.CharField(max_length=512)

    def _name(self):
        return self.name


class CIF(BaseModel):

    class Meta:
        verbose_name_plural = 'Central Instruments Facility'

    equipment_name = RichTextField()
    equipment_desc = RichTextField()
    image = models.ImageField(upload_to=rename_image_cif_photo)

    def _equipment_name(self):
        return self.equipment_name

    def _equipment_desc(self):
        return self.equipment_desc

class PCBD(BaseModel):
    c_number = models.CharField(max_length=120)
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=300)
    mobile = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{10}$')])
    cat = models.CharField(max_length=10)
    address = RichTextField()
    complaint = RichTextField()
    replytxt = RichTextField(default='', blank=True)
    replyurl = models.FileField(upload_to="facilities/pcbdfile/%Y", blank=True)

class Logocomp(BaseModel):
    name = models.CharField(max_length=1024)
    guardian = models.CharField(max_length=1024)
    stdtype = models.CharField(max_length=1024, blank=True)
    identity = models.CharField(max_length=1024, blank=True)
    mobile = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{10}$')])
    email = models.CharField(max_length=1024)
    logoimg = models.ImageField(upload_to='logocomp/logos/',validators=[FileExtensionValidator(allowed_extensions=['gif','png','jpg'])])
