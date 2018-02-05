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
