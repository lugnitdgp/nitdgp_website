from django.db import models

# Create your models here.
from base.models import BaseModel


def last_count():
    return Section.objects.count()+1


class Section(BaseModel):

    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=last_count)

    def __str__(self):
        return self.name


class Content(BaseModel):

    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section)
    icon = models.CharField(max_length=100)
    row = models.CharField(max_length=100)
    link = models.URLField(max_length=128, unique=True)

    def __str__(self):
        return self.name
