from django.db import models

# Create your models here.
from base.models import BaseModel


def next_count_section():
    return Section.objects.count()+1


class Section(BaseModel):

    name = models.CharField(max_length=100)
    priority = models.PositiveSmallIntegerField(default=next_count_section, unique=True)

    def __str__(self):
        return self.name

    def _priority(self):
        return self.priority

    def _tiles(self):
        return list(Tile.objects.all().filter(section__name__iexact=self.name))

    class Meta:
        ordering = ('priority',)


class Tile(BaseModel):

    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()
    link = models.URLField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def _section(self):
        return self.section.name

    def _row(self):
        return self.row

    def _column(self):
        return self.column

    class Meta:
        ordering = ('section', 'row', 'column', 'name')


class Carousel(BaseModel):

    primary_caption = models.CharField(max_length=255)
    secondary_caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='carousel/%Y')

    def __str__(self):
        return self.primary_caption

    def _secondary(self):
        return self.secondary_caption

    def _image(self):
        return self.image
