from django.db import models
from base.models import BaseModel
from department.models import Faculty

# Create your models here.


class BOG(BaseModel):

    class Meta:
        verbose_name_plural = 'BOG'

    ROLE_TYPES = (('Chairperson', 'Chairperson'), ('Secretary', 'Secretary'), ('Member', 'Member'))
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_TYPES, default='Member', max_length=20)

    def _role(self):
        return self.role

    def _name(self):
        return self.faculty.name


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
