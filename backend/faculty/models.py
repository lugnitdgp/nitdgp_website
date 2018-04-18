from django.db import models
from base.models import BaseModel
from ckeditor.fields import RichTextField
from department.models import Faculty

class GeneralInformation(BaseModel):

    class Meta:
        verbose_name_plural = 'General Information'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    education = RichTextField()
    work_experience = RichTextField()
    projects = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _department(self):
        return self.faculty.department.name

    def _education(self):
        return self.education

    def _work_experience(self):
        return self.work_experience

    def _projects(self):
        return self.projects
