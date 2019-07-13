import datetime
from haystack import indexes
from academics.models import Notice, HostelNotice
from department.models import Faculty


class NoticeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    notice_type = indexes.CharField(model_attr='notice_type')
    date = indexes.DateTimeField(model_attr='date')

    def get_model(self):
        return Notice

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date__lte=datetime.datetime.now())


class HostelNoticeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    notice_type = indexes.CharField(model_attr='hall_type')
    date = indexes.DateTimeField(model_attr='date')

    def get_model(self):
        return HostelNotice

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date__lte=datetime.datetime.now())


class FacultyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    designation = indexes.CharField(model_attr='designation')

    def get_model(self):
        return Faculty
