from django.db import models
from base.models import BaseModel


class Library(BaseModel):

    class Meta:
        verbose_name_plural = 'Library'

    home = models.TextField()
    about = models.TextField()
    contact_us = models.TextField()

    def _home(self):
        return self.home

    def _about(self):
        return self.about

    def _contact_us(self):
        return self.contact_us


class EResource(BaseModel):

    class Meta:
        verbose_name_plural = 'E Resources'

    title = models.CharField(max_length=255, default="")
    url = models.URLField()

    def __str__(self):
        return self.title

    def _url(self):
        return self.url

class SAC(BaseModel):

    class Meta:
        verbose_name_plural = 'S A C'

    about = models.TextField()
    mission = models.CharField(max_length=1024,default="")
    vision = models.CharField(max_length=1024,default="")
    program_offered = models.CharField(max_length=1024,default="")
    other_activities = models.TextField()
    facility = models.TextField()
    contact_us = models.TextField()
    ach_url = models.URLField()#for adding the link of the record of all the achievements of NIT DGP
    rec_url = models.URLField() #for adding the link of the record of sports and games in NIT DGP

    def _about(self):
        return self.about

    def __str__(self):
        return self.mission

    def __str__(self):
        return self.vision

    def __str__(self):
        return self.program_offered

    def _other_activities(self):
        return self.other_activities

    def _facility(self):
        return self.facility

    def _contact_us(self):
        return self.contact_us

    def _ach_url(self):
        return self.ach_url

    def _rec_url(self):
        return self.rec_url
