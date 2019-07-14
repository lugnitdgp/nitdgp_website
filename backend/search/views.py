from datetime import date

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet, EmptySearchQuerySet

from search.serializers import NoticeSearchSerializer
from search.serializers import FacultySearchSerializer
from academics.models import Notice, HostelNotice
from department.models import Faculty


class NoticeSearchViewSet(ListAPIView):
    serializer_class = NoticeSearchSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        request = self.request
        queryset = EmptySearchQuerySet()

        if request.GET.get('q', ''):
            query = request.GET.get('q', '')
            queryset = SearchQuerySet().models(Notice, HostelNotice).filter(
                content=query).order_by('-date')
            return [i.object for i in queryset]


class FacultySearchViewSet(ListAPIView):
    serializer_class = FacultySearchSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        request = self.request
        queryset = EmptySearchQuerySet()

        if request.GET.get('q', ''):
            query = request.GET.get('q', '')
            queryset = SearchQuerySet().models(Faculty).filter(content=query)
            return [i.object for i in queryset]
