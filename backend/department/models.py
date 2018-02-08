import datetime
import os
import shutil

from django.db import models
from ckeditor.fields import RichTextField

from base.models import BaseModel
from root.settings import BASE_DIR


class Department(BaseModel):
    name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=4)
    about_us =  RichTextField()
    mission = RichTextField()
    vision = RichTextField()
    contact_us = RichTextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        dept_dir = os.path.join(os.path.dirname(BASE_DIR), 'departments')
        try:
            os.makedirs(os.path.join(dept_dir, self.short_code.lower()))
            shutil.copy(os.path.join(dept_dir, 'dummy.html'),
                        os.path.join(dept_dir, self.short_code.lower(), 'index.html'))
            super(Department, self).save(*args, **kwargs)
        except (FileNotFoundError, OSError):  # Handle the error properly
            pass


def rename_image(instance, filename):

    return 'faculty/{0}/{1}'.format(instance.name, filename)


class Faculty(BaseModel):

    class Meta:
        verbose_name_plural = 'Faculty'

    YEAR_CHOICES = [(r, r) for r in range(1965, datetime.date.today().year+1)]
    name = models.CharField(max_length=255)
    research_interest = RichTextField()
    email = models.CharField(max_length=255, default="")
    mobile = models.BigIntegerField(null=True)
    joining_year = models.CharField(max_length=4, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    image = models.ImageField(upload_to=rename_image)

    def __str__(self):
        return self.name

    def _department(self):
        return self.department.name


class Research(BaseModel):

    class Meta:
        verbose_name_plural = 'Research'

    YEAR_CHOICES = [(r, r) for r in range(1965, datetime.date.today().year+1)]
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    collab_inst = RichTextField()
    area = RichTextField()
    faculty_involved = RichTextField()
    date = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return self.area

    def _institute_involved(self):
        return self.collab_inst

    def _department(self):
        return self.department.name

    def _faculty_involved(self):
        return self.faculty_involved

    def _date(self):
        return self.date


class Project(BaseModel):

    YEAR_CHOICES = [(r, r) for r in range(1965, datetime.date.today().year+1)]
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    collab_inst = RichTextField()
    area = RichTextField()
    faculty_involved = RichTextField()
    funding = models.CharField(max_length=56)
    date = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

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

    def _date(self):
        return self.date


class Roles(BaseModel):

    class Meta:
        verbose_name_plural = 'Roles'

    ROLE_TYPES = (('Departmental', 'Departmental'), ('Administrative', 'Administrative'))
    name = models.CharField(max_length=56)
    type = models.CharField(choices=ROLE_TYPES, default='Departmental', max_length=30)

    def __str__(self):
        return self.name


class FacultyRoles(BaseModel):

    class Meta:
        verbose_name_plural = 'Faculty Roles'

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def _faculty(self):
        return self.faculty.name

    def _role(self):
        return self.role.name

    def _department(self):
        return self.faculty.department.name


class Activity(BaseModel):

    class Meta:
        verbose_name_plural = 'Activities'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    speakers = models.CharField(max_length=512)
    programme = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def _department(self):
        return self.department.name

    def _speakers(self):
        return self.speakers

    def _programme(self):
        return self.programme

    def _start_date(self):
        return self.start_date

    def _end_date(self):
        return self.end_date


class Degree(BaseModel):

    class Meta:
        verbose_name_plural = 'Degree'

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name

    def _description(self):
        return self.description


class Programme(BaseModel):

    class Meta:
        verbose_name_plural = 'Programmes'

    title = models.CharField(max_length=255)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def _title(self):
        return self.title

    def _degree(self):
        return self.degree.name

    def _department(self):
        return self.department.name


class Courses(BaseModel):

    class Meta:
        verbose_name_plural = 'Courses'

    COURSE_TYPES = (('L', 'Lecture'), ('T', 'Tutorial'), ('S', 'Sessional'))
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    short_code = models.CharField(max_length=7)
    semester = models.IntegerField()
    course_type = models.CharField(choices=COURSE_TYPES, default='L', max_length=30)
    credits = models.IntegerField()

    def __str__(self):
        return self.programme.title

    def _programme(self):
        return self.programme.title

    def _short_code(self):
        return self.short_code

    def _semester(self):
        return self.semester

    def _course_type(self):
        return self.course_type


class Facility(BaseModel):

    class Meta:
        verbose_name_plural = 'Facilities'

    FACILITY_CHOICES = (('Laboratory', 'Laboratory'), ('Equipment', 'Equipment'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(choices=FACILITY_CHOICES, max_length=15)

    def __str__(self):
        return self.name

    def _department(self):
        return self.department.name

    def _category(self):
        return self.category


class Electives(BaseModel):

    class Meta:
        verbose_name_plural = 'Electives'

    short_code = models.CharField(max_length=7)
    title = models.CharField(max_length=200)
    is_open = models.BooleanField(default=True)
    semester = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def _department(self):
        return self.department.name

    def _title(self):
        return self.title

    def _semester(self):
        return self.semester

    def _is_open(self):
        return self.is_open


def rename_image_department_photo(instance, filename):

    return 'department/{0}/images/{1}'.format(instance.department.short_code, filename)


class DepartmentPhotos(BaseModel):

    class Meta:
        verbose_name_plural = 'Department Photos'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to=rename_image_department_photo)

    def _department(self):
        return self.department.name

    def _title(self):
        return self.title

    def _date(self):
        return self.date


def rename_image_department_news(instance, filename):

    return 'department/{0}/news/{1}'.format(instance.department.short_code, filename)


class DepartmentNews(BaseModel):

    class Meta:
        verbose_name_plural = 'Department News'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    link = models.FileField(upload_to=rename_image_department_news)

    def _department(self):
        return self.department.name

    def _title(self):
        return self.title

    def _date(self):
        return self.date
