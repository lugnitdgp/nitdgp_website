from django.db import models

# Create your models here.
from base.models import BaseModel

def next_count():
    return Section.objects.count()+1


class Section(BaseModel):

    name = models.CharField(max_length=100)
    priority = models.PositiveSmallIntegerField(default=next_count, unique=True)

    def __str__(self):
        return self.name

    def _priority(self):
        return self.priority

    def _tiles(self):
        return list(Tile.objects.all().filter(section__name__iexact=self.name))

    class Meta():
        ordering = ('priority',)


class Tile(BaseModel):

    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    row = models.CharField(max_length=100)
    link = models.URLField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def _section(self):
        return self.section.name

    def _row(self):
        return self.row

    class Meta():
        ordering = ('section', 'row', 'name',)
