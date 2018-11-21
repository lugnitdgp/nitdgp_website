from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from faculty.serializers import *
from department.models import Faculty
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import tempfile
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
            file_name = qset.note.path
            old_cwd = os.getcwd()
            file_extension = "." + file_name.split('.')[-1]
            dir_name = os.path.dirname(file_name)
            print(file_name, dir_name)
            os.chdir(dir_name)
            tmp = tempfile.NamedTemporaryFile(
                mode="wb+",
                dir=dir_name,
                delete=False,
                prefix="NOTES-",
                suffix=file_extension
            )
            tmp.write(qset.note.read())
            tmp_file_name = tmp.name
            download_file_name = "/".join(qset.note.url.split('/')[0:-1]) + "/" + os.path.basename(tmp.name)
            tmp.close()
            os.chmod(tmp_file_name, 0o640)
            os.chdir(old_cwd)
            return HttpResponse(
                json.dumps({"download_url": download_file_name}),
                content_type="application/json"
            )
        else:
            return HttpResponse(status=403)
    return HttpResponse(status=404)
