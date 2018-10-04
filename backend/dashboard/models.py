from django.db import models
from base.models import BaseModel
from ckeditor.fields import RichTextField


def next_count_section():
    return Section.objects.count()+1


class QuickLinks(BaseModel):

    class Meta:
        verbose_name_plural = 'Quick Links'

    CHOICES = (
        ('General', 'General'),
        ('Admission', 'Admission'),
        ('Social Media', 'Social Media'),
        ('National Portal', 'National Portal')
    )
    title = models.CharField(max_length=1024)
    file = models.FileField(upload_to='dashboard/quick_links/%Y/%m/%d', blank=True)
    link = models.URLField(blank=True)
    category = models.CharField(max_length=64, choices=CHOICES, default='General')

    def __str__(self):
        return self.title


class Downloads(BaseModel):
    class Meta:
        verbose_name_plural = 'Downloads'

    title = models.CharField(max_length=1024)
    file = models.FileField(upload_to='dashboard/downloads/%Y/%m/%d')

    def __str__(self):
        return self.title


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


class Event(BaseModel):

    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='events/%Y/%m/%d')

    def __str__(self):
        return self.title

    def _file(self):
        return self.file


class NewsFeed(BaseModel):

    class Meta:
        verbose_name_plural = 'News Feed'

    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='newsfeed/%Y/%m/%d', blank=True)
    url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    def _file(self):
        return self.file

    def _date(self):
        return self.date


class Contact(BaseModel):

    class Meta:
        verbose_name_plural = 'Contact Us'

    GROUPS = (
        ('Academic Qualification Verification', 'Academic Qualification Verification'),
        ('Associate Dean', 'Associate Dean'),
        ('Computer Center', 'Computer Center'),
        ('Dean', 'Dean'),
        ('Director', 'Director'),
        ('Director Office', 'Director Office'),
        ('Guest House', 'Guest House'),
        ('HOD', 'HOD'),
        ('Library', 'Library'),
        ('Medical Unit', 'Medical Unit'),
        ('Officers', 'Officers'),
        ('Pension Cell', 'Pension Cell'),
        ('Registrar', 'Registrar'),
        ('Registrar Office', 'Registrar Office'),
        ('Training and Placement', 'Training and Placement'),
        ('Warden', 'Warden'),
        ('Workshops', 'Workshops')
    )
    name = models.CharField(max_length=512)
    designation = models.CharField(max_length=512,blank=True)
    group = models.CharField(choices=GROUPS, max_length=512)
    contact = RichTextField()

    def _name(self):
        return self.name

    def _designation(self):
        return self.designation

    def _group(self):
        return self.group

    def _contact(self):
        return self.contact


class HitCount(models.Model):

    count = models.IntegerField(default=0)
