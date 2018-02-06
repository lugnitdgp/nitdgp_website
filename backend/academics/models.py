from django.db import models
from base.models import BaseModel

# Create your models here.


class Notice(BaseModel):
    title = models.CharField(max_length=512)
    link = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.title

    def _link(self):
        return self.link

    def _date(self):
        return self.date
