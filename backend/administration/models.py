from django.db import models
from django.core.validators import RegexValidator
from base.models import BaseModel
from department.models import Faculty

class Dean(BaseModel):

    class Meta:
        ordering = ('-role', 'seniority')

    ROLE_TYPES = (('Dean', 'Dean'), ('Associate Dean', 'Associate Dean'))
    designation = models.CharField(max_length=512)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_TYPES, max_length=100)
    seniority = models.IntegerField(choices=[(i, i) for i in range(1,7)])

    def ___str__(self):
        return self.faculty.name

    def _designation(self):
        return self.designation

    def _role(self):
        return self.role

    def _email(self):
        return self.faculty.email

    def _image(self):
        return self.faculty.image


class Warden(BaseModel):

    class Meta:
        ordering = ('-role', 'designation')

    ROLE_TYPES = (('chief_warden', 'Chief Warden'), ('associate_chief_warden', 'Associate Chief Warden'), ('warden', 'Warden'))
    designation = models.CharField(max_length=512)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_TYPES, max_length=100)

    def ___str__(self):
        return self.faculty.name

    def _designation(self):
        return self.designation

    def _role(self):
        return self.role

    def _email(self):
        return self.faculty.email

    def _image(self):
        return self.faculty.image

class BOG(BaseModel):

    class Meta:
        verbose_name_plural = 'Board Of Governors'

    ROLE_TYPES = (('Chairperson', 'Chairperson'), ('Secretary', 'Secretary'), ('Member', 'Member'))
    name = models.CharField(max_length=512)
    role = models.CharField(choices=ROLE_TYPES, default='Member', max_length=20)
    designation = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='administration/bog')

    def _role(self):
        return self.role

    def _name(self):
        return self.name

    def _role(self):
        return self.role

    def _designation(self):
        return self.designation

    def _address(self):
        return self.address


class BogAgenda(BaseModel):

    class Meta:
        verbose_name_plural = 'BOG Agenda for Meetings'
        ordering = ('-date',)

    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='academics/notices/%Y/%m/%d')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _date(self):
        return self.date


class BwcIfc(BaseModel):

    class Meta:
        verbose_name_plural = 'BWC'

    TYPE_CHOICES = (
        ('BWC', 'BWC'),
        ('IFC', 'IFC'),
    )

    title = models.CharField(max_length=512)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='administration/bwc/%Y/%m/%d')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _type(self):
        return self.type

    def _file(self):
        return self.file

    def _date(self):
        return self.date

    class Meta:
        ordering = ('-date',)

class Senate(BaseModel):

    class Meta:
        verbose_name_plural = 'Senate Meetings'
        ordering = ('-date', )

    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='administration/senate/%Y/%m/%d')
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _date(self):
        return self.date


class Officer(BaseModel):
    class Meta:
        ordering = ('designation', 'name')

    name = models.CharField(max_length=512)
    designation = models.CharField(max_length=512)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$')],
        blank=True
    )
    mobile = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$')],
        blank=True
    )
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='administration/officer/')
