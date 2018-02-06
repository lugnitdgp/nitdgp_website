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


class E_resource(BaseModel):
    """E-resourses for library"""
    title = models.CharField(max_length=255, default="E Res")
    url = models.CharField(max_length=255, default="https://www.google.com")

    def __str__(self):
        return self.title

    def _title(self):
        return self.title

    def _url(self):
        return self.url
