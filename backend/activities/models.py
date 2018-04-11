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


class SeminarEvent(BaseModel):

	class Meta:
		verbose_name_plural = 'Seminar and Events'
		ordering = ('-date', )

	title = models.CharField(max_length=512)
	file = models.FileField(upload_to='activities/seminar_and_events/%Y/%m/%d')
	date = models.DateField()

	def _title(self):
		return self.title

	def _file(self):
		return self.file

	def _date(self):
		return self.date
