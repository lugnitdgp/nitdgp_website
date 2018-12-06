from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.core import serializers

from information.models import Tender,Career
from academics.models import Notice
from activities.models import SeminarEvent


class APIRoot(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        resp_dict = {
            'dashboard': reverse('dashboard:list-tile-content', request=request),
            'department': reverse('department:list-department', request=request),
        }

        return Response(resp_dict)


def convert_url(f, r):
    return r.build_absolute_uri(f.url) if f.name != "" else f.name


def archives(request):
    serializerTender = list(map(lambda x: {
        'title': x.title,
        'date': x.date,
        'file': convert_url(x.file, request)
    }, list(Tender.objects.filter(archive=True).order_by('-date'))))

    serializerCareer = list(map(lambda x: {
        'title': x.title,
        'date': x.date,
        'file': convert_url(x.file, request)
    }, list(Career.objects.filter(archive=True).order_by('-date'))))

    serializerAcademicNotice = list(map(lambda x: {
        'title': x.title,
        'date': x.date,
        'file': convert_url(x.file, request),
        'url': x.url
    }, list(Notice.objects.filter(archive=True,notice_type='Academic').order_by('-date'))))

    serializerStudentNotice = list(map(lambda x: {
        'title': x.title,
        'date': x.date,
        'file': convert_url(x.file, request),
        'url': x.url
    }, list(Notice.objects.filter(archive=True,notice_type='Student').order_by('-date'))))

    serializerGeneralNotice = list(map(lambda x: {
        'title': x.title,
        'date': x.date,
        'file': convert_url(x.file, request),
        'url': x.url
    }, list(Notice.objects.filter(archive=True,notice_type='General').order_by('-date'))))

    serializerEvent = list(map(lambda x: {
        'title': x.title,
        'date': x.date,
        'file': convert_url(x.file, request),
        'url': x.url
    }, list(SeminarEvent.objects.filter(archive=True).order_by('-date'))))

    json = {
        "tender": serializerTender,
        "academic_notice": serializerAcademicNotice,
        "student_notice": serializerStudentNotice,
        "general_notice": serializerGeneralNotice,
        "career":serializerCareer,
        "event":serializerEvent
    }

    return JsonResponse(json)
