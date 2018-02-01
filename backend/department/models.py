from django.db import models
from base.models import BaseModel
import datetime
import uuid


class Department(BaseModel):
    name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=4)
    about_us = models.TextField()
    mission = models.CharField(max_length=255)
    vision = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Faculty(BaseModel):

    class Meta:
        verbose_name_plural = 'Faculties'

    name = models.CharField(max_length=255)
    research_interest = models.TextField()
    email = models.CharField(max_length=255, default="")
    mobile = models.BigIntegerField(max_length=10, null=True)
    joining_year = models.CharField(max_length=4, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def _department(self):
        return self.department.name


class Research(BaseModel):

    class Meta:
        verbose_name_plural = 'Research'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    collab_inst = models.TextField()
    area = models.CharField(max_length=255)
    faculty_involved = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.area

    def _institute_involved(self):
        return self.collab_inst

    def _department(self):
        return self.department.name

    def _faculty_involved(self):
        return self.faculty_involved

class Project(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    collab_inst = models.TextField()
    area = models.CharField(max_length=255)
    faculty_involved = models.TextField()
    funding = models.CharField(max_length=56)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.area

    def _institute_involved(self):
        return self.collab_inst

    def _department(self):
        return self.department.name

    def _faculty_involved(self):
        return self.faculty_involved

    def _funding(self):
        return self.funding

class Roles(BaseModel):
    name = models.CharField(max_length=56)

class FacultyRoles(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Activites(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    speakers = models.CharField(max_length=512)
    programme = models.TextField()
    date = models.DateField(auto_now_add=True)

class Degree(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)

class Programme(BaseModel):
    title = models.CharField(max_length=255)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Courses(BaseModel):
    COURSE_TYPES = (('1','L'), ('2','T'), ('3','S'))
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    short_code = models.CharField(max_length=7)
    semester = models.IntegerField()
    course_type = models.IntegerField(choices=COURSE_TYPES, default=1)
    credits = models.IntegerField()

class Facilities(BaseModel):
    FACILITY_CHOICES = (('1','Laboratory'), ('2','Equipment'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=FACILITY_CHOICES, default=1)

class Electives(BaseModel):
    short_code = models.CharField(max_length=7)
    title = models.CharField(max_length=200)
    is_open = models.BooleanField(default=True)
    semester = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class DepartmentPhotos(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=255)

class DepartmentNews(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)