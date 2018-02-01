from django.db import models
import datetime
import uuid


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255)
    short_code=models.CharField(max_length=4)
    about_us=models.TextField()

    def __str__(self):
        return self.name


class Faculty(models.Model):

    class Meta:
        verbose_name_plural = 'Faculties'

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255)
    research_interest=models.TextField()
    email=models.CharField(max_length=255, default="")
    mobile=models.CharField(max_length=10, null=True)
    joining_year=models.CharField(max_length=4, null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def _department(self):
        return self.department.name


class Research(models.Model):

    class Meta:
        verbose_name_plural = 'Research'

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    collab_inst=models.TextField()
    area=models.CharField(max_length=255)
    faculty_involved=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.area

    def _institute_involved(self):
        return self.collab_inst

    def _department(self):
        return self.department.name

    def _faculty_involved(self):
        return self.faculty_involved


class Electives(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    short_code=models.CharField(max_length=7) #for example if an elective is MME 461 total size is 7 including the space
    title=models.CharField(max_length=200)
    is_open=models.BooleanField(default=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

class FacultyRoles(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    #role=models.ForeignKey(Roles,on_delete=models.CASCADE)

# class Roles(models.Model):
# # Create your models here.
#     pass
