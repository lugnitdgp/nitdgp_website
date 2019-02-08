from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from faculty.serializers import *
from department.models import Faculty
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from root import settings
import tempfile
from shutil import copyfile
import os
import json


class FacultyViewSet(RetrieveAPIView):

    queryset = Faculty.objects.all()
    serializer_class = FacultyDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response({"faculty": FacultyDetailSerializer(self.get_queryset().filter(id=kwargs['pk']), many=True, context={'request': request}).data
        })


@csrf_exempt
def download_note(request):
    if request.POST.get('input_key', False) and request.POST.get('id', False):
        try:
            qset = Notes.objects.get(id=request.POST['id'])
        except Notes.DoesNotExist:
            return HttpResponse(status=404)
        if qset.secret_key == request.POST.get('input_key', ""):
            # Get file name from db
            absolute_file = qset.note.path
            file_name = absolute_file.split('/')[-1]

            # Create a temp directory
            os.makedirs(settings.MEDIA_ROOT + "/tmp", exist_ok=True)
            tmp_dir = tempfile.TemporaryDirectory(
                prefix="download-notes-",
                dir=settings.MEDIA_ROOT + "/tmp"
            ).name
            os.mkdir(tmp_dir)
            tmp_file = tmp_dir + "/" + file_name

            # Copy the file over to the temp directory
            copyfile(absolute_file, tmp_file)

            # Generate and send the download URL as a response
            download_file_name = ("/".join(qset.note.url.split('/')[0:2]) +
                                  "/tmp" +
                                  "/" + os.path.basename(tmp_dir) +
                                  "/" + file_name)
            return HttpResponse(
                json.dumps({"download_url": download_file_name}),
                content_type="application/json"
            )
        else:
            return HttpResponse(status=403)
    return HttpResponse(status=404)
