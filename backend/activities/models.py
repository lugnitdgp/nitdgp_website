from django.db import models
from base.models import BaseModel
from ckeditor.fields import RichTextField


class StudentClub(BaseModel):

	class Meta:
		verbose_name_plural = 'Student Clubs and Technical Activities'
		ordering = ('name', )

	name = models.CharField(max_length=512)
	image = models.ImageField(upload_to='activities/student_clubs/')
	description = RichTextField()
	link = models.URLField()

	def _name(self):
		return self.name

	def _description(self):
		return self.description

	def _link(self):
		return self.link


class Festival(BaseModel):

	class Meta:
		verbose_name_plural = 'Festivals'
		ordering = ('name', )

	name = models.CharField(max_length=512)
	image = models.ImageField(upload_to='activities/student_festivals/')
	description = RichTextField()
	link = models.URLField()

	def _name(self):
		return self.name

	def _description(self):
		return self.description

	def _link(self):
		return self.link


class GrievanceCell(BaseModel):
	class Meta:
		verbose_name_plural = 'Grievance Cell'
		ordering = ('-date', )

	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/grievance_cell/%Y/%m/%d', blank=True)
	url = models.URLField(blank=True)
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _url(self):
		return self.url

	def _date(self):
		return self.date


class SeminarEvent(BaseModel):

	class Meta:
		verbose_name_plural = 'Seminar and Events'
		ordering = ('-date', )

	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/seminar_and_events/%Y/%m/%d', blank=True)
	archive = models.BooleanField(default=False)
	url = models.URLField(blank=True)
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _url(self):
		return self.url

	def _date(self):
		return self.date


class Achievement(BaseModel):

	class Meta:
		verbose_name_plural = 'Achievements'
		ordering = ('-date', )

	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/achievements/%Y/%m/%d')
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _date(self):
		return self.date


class Research(BaseModel):

	class Meta:
		verbose_name_plural = 'Research'
		ordering = ('-date', )

	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/research/%Y/%m/%d', blank=True)
	url = models.URLField(blank=True)
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _date(self):
		return self.date

	def _url(self):
		return self.url


class Visitor(BaseModel):

	class Meta:
		verbose_name_plural = 'Event Visitors'
		ordering = ('-created_at', )

	name = models.CharField(max_length=512)
	designation = models.CharField(max_length=1024)
	event_name = models.CharField(max_length=1024)
	image = models.ImageField(upload_to='activites/event_visitors/%Y/%m/%d')

	def _name(self):
		return self.name

	def _designation(self):
		return self.designation

	def _event_name(self):
		return self.event_name


class PlacementLinks(BaseModel):

	class Meta:
		verbose_name_plural = 'Important Links for Placement'
		ordering = ('-date',)

	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/placement_links/%Y/%m/%d', blank=True)
	url = models.URLField(blank=True)
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _date(self):
		return self.date

	def _url(self):
		return self.url


class Placement(BaseModel):

	class Meta:
		verbose_name_plural = 'Placement'
		ordering = ('-date', )

	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/placement/%Y/%m/%d', blank=True)
	url = models.URLField(blank=True)
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _date(self):
		return self.date

	def _url(self):
		return self.url

class Collaboration(BaseModel):

	class Meta:
		verbose_name_plural = 'Collaboration'
		ordering = ('-date', )
	COLLABLIST = (('National','National'),('International','International'))
	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/collaboration/%Y/%m/%d', blank=True)
	type = models.CharField(choices=COLLABLIST,default='National',max_length=512)
	url = models.URLField(blank=True)
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _type(self):
		return self.type

	def _date(self):
		return self.date

	def _url(self):
		return self.url

class Brics(BaseModel):

	class Meta:
		verbose_name_plural = 'Brics'
		ordering = ('-created_at', )

	title = models.CharField(max_length=255)
	file = models.FileField(upload_to='activities/brics/%Y')
	date = models.DateField()

	def __str__(self):
		return self.title

	def _file(self):
		return self.file

	def _date(self):
		return self.date

class Coe(BaseModel):

	class Meta:
		verbose_name_plural = 'Center of Excellence'
		ordering = ('name', )

	name = models.CharField(max_length=512)
	image = models.ImageField(upload_to='activities/coe/%Y')
	description = RichTextField()
	link = models.URLField()

	def _name(self):
		return self.name

	def _description(self):
		return self.description

	def _link(self):
		return self.link

class Coecarousel(BaseModel):

	class Meta:
		verbose_name_plural = 'CoE Carousel Images'
	COES = (('CARE','CARE'),('CREW','CREW'),('AM','AM'),('IOTIS','IOTIS'),('RAA','RAA'),('NCC','NCC'),('NSS','NSS'),('UBA','UBA'),('FIM','FIM'))
	primary_caption = models.CharField(max_length=255)
	secondary_caption = models.CharField(max_length=255)
	coe_type = models.CharField(choices=COES,default='CREW',max_length=255)
	image = models.ImageField(upload_to='coecarousel/%Y')

	def __str__(self):
		return self.primary_caption

	def _secondary(self):
		return self.secondary_caption
	
	def _type(self):
		return self.coe_type
		
	def _image(self):
		return self.image


def outreach_icon_path(instance, filename):
	return 'activities/outreach/{0}/icon-{1}'.format(
		instance.category.replace('/', '_slash_'),
		instance.name.replace('/', '_slash_') + ' - ' + filename.replace('/', '_slash_')
	)


def outreach_mou_path(instance, filename):
	return 'activities/outreach/{0}/mou-{1}'.format(
		instance.category.replace('/', '_slash_'),
		instance.name.replace('/', '_slash_').replace('-', '_') + '-' + filename.replace('/', '_slash_').replace('-', '_')
	)


class Outreach(BaseModel):
	class Meta:
		verbose_name_plural = 'Outreach'
		ordering = ('category', 'name')
	OUTREACH_CATEGORIES = (
		("Colleges/Institutes/Universities (Abroad)", "Colleges/Institutes/Universities (Abroad)"),
		("Colleges/Institutes/Universities (India)", "Colleges/Institutes/Universities (India)"),
		("Industries/Organizations (India)", "Industries/Organizations (India)"),
		("Research Institutions (India)", "Research Institutions (India)")
	)
	category = models.CharField(choices=OUTREACH_CATEGORIES, max_length=512, blank=False)
	name = models.CharField(max_length=512, blank=False)
	mou = models.FileField(upload_to=outreach_mou_path, blank=False)
	icon = models.FileField(upload_to=outreach_icon_path, blank=False)


class Newsletter(BaseModel):
	class Meta:
		verbose_name_plural = 'Newsletters'

	title  = models.CharField(max_length=255)
	file = models.FileField(upload_to='activities/newsletters/%Y', blank=True)
	link = models.URLField(blank=True)
	date = models.DateField()

	def __str__(self):
		return self.title

class Covid(BaseModel):
	class Meta:
		verbose_name_plural = "Covid-19 info"

	title = models.CharField(max_length=255)
	file = models.FileField(upload_to='activities/covid/%Y', blank=True)
	link = models.URLField(blank=True)
	date = models.DateField()

	def __str__(self):
		return self.title