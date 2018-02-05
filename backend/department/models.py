from django.db import models
from base.models import BaseModel


class Department(BaseModel):
    name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=4)
    about_us = models.TextField()
    mission = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.name


class Faculty(BaseModel):

    class Meta:
        verbose_name_plural = 'Faculty'

    name = models.CharField(max_length=255)
    research_interest = models.TextField()
    email = models.CharField(max_length=255, default="")
    mobile = models.BigIntegerField(null=True)
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


class Activites(BaseModel):

    class Meta:
        verbose_name_plural = 'Activites'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    speakers = models.CharField(max_length=512)
    programme = models.TextField()
    date = models.DateField(auto_now_add=True)

    def _department(self):
        return self.department.name

    def _speakers(self):
        return self.speakers

    def _programme(self):
        return self.programme

    def _date(self):
        return self.date


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
    category = models.CharField(choices=FACILITY_CHOICES, max_length=1)

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


class DepartmentPhotos(BaseModel):

    class Meta:
        verbose_name_plural = 'Department Photos'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=255)

    def _department(self):
        return self.department.name

    def _title(self):
        return self.title

    def _date(self):
        return self.date


class DepartmentNews(BaseModel):

    class Meta:
        verbose_name_plural = 'Department News'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def _department(self):
        return self.department.name

    def _title(self):
        return self.title

    def _date(self):
        return self.date
