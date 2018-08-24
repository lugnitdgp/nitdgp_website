from django.db import models
from base.models import BaseModel
from ckeditor.fields import RichTextField
from department.models import Faculty, Courses

class Teachings(BaseModel):

    class Meta:
        verbose_name_plural = 'Teachings'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    teachings = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _teachings(self):
        return self.teachings


class AdministrativeResponsibility(BaseModel):

    class Meta:
        verbose_name_plural = 'Administrative Responsibilities'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    administrative_responsibilities = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _administrative_responsibilities(self):
        return self.administrative_responsibilities


class AwardsAndRecognition(BaseModel):

    class Meta:
        verbose_name_plural = 'Awards and Recognition'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    awards_and_recognition = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _awards_and_recognition(self):
        return self.awards_and_recognition


class Education(BaseModel):

    class Meta:
        verbose_name_plural = 'Education'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    education = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _education(self):
        return self.education


class WorkExperience(BaseModel):

    class Meta:
        verbose_name_plural = 'Work Experience'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    work_experience = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _work_experience(self):
        return self.work_experience


class Projects(BaseModel):

    class Meta:
        verbose_name_plural = 'Projects'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    projects = RichTextField()

    def __str__(self):
        return self.faculty.name

    def _projects(self):
        return self.projects


def rename_students(instance, filename):

    return 'faculty/{0}/students/{1}'.format(instance.faculty_id.name, filename)


class Students(BaseModel):

    class Meta:
        verbose_name_plural = 'Students under Faculty'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to=rename_students)

    def __str__(self):
        return self.faculty_id.name

    def _title(self):
        return self.title

    def _file(self):
        return self.file
