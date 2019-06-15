from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.core.mail import send_mail
from django.http import HttpResponse
from facilities.serializers import *
from facilities.models import *
import json


class CentersViewSet(ListAPIView):
        queryset = Center.objects.all().order_by('title')
        serializer_class = CentersSerializer

        def list(self, request, *args, **kwargs):
            return Response({"centers": CentersSerializer(self.get_queryset(), many=True, context={"request": request}).data
            })


class LibraryViewSet(ListAPIView):

	queryset = Library.objects.all().order_by('-updated_at')[:1]
	serializer_class = LibrarySerializer


class ResourceViewSet(ListAPIView):

	queryset = Resource.objects.all()
	serializer_class = ResourceSerializer

	def list(self, request, *args, **kwargs):
		result = {}
		for resource in self.get_queryset():
			rtype = resource.type
			if rtype in result:
				result[rtype].append(ResourceSerializer(resource, context={"request": request}).data)
			else:
				result[rtype] = [ResourceSerializer(resource, context={"request": request}).data]
		return Response({"resources": result})

class SemesterquestionViewSet(ListAPIView):
    queryset = Semesterquestion.objects.all().order_by('-updated_at')
    serializer_class = SemesterquestionSerializer



class SACViewSet(ListAPIView):

	queryset = SAC.objects.all().order_by('-updated_at')[:1]
	serializer_class = SACSerializer


class HostelViewSet(ListAPIView):
	queryset = Hostel.objects.all().order_by('name')
	serializer_class = HostelSerializer


class CIFViewSet(ListAPIView):
	queryset = CIF.objects.all()
	serializer_class = CIFSerializer

class PCBDViewSet(ListAPIView):
	queryset = PCBD.objects.all()
	serializer_class = PCBDSerializer

@csrf_exempt
def pcbdcomplaint(request, **kwarg):
	if request.method == 'POST':
		QueryDict = request.POST
		values = QueryDict.dict()
		qry = PCBD.objects.filter(email=values['email'])
		if qry:
			return HttpResponse(
                json.dumps({"message": 'Already Register'}),
                content_type="application/json"
            )
			pass
		else:
			stud_name = values['name']
			stud_email = values['email']
			stud_c_number = values['c_number']
			stud_complaint = values['complaint']
			stud_cat = values['cat']
			emailtitle = 'Prevent Caste Base Descrimination complaint Number '+stud_c_number
			if values:
				PCBD.objects.create(**values)
				send_mail(
				    emailtitle,
				    stud_complaint,
				    'webmaster@nitdgp.ac.in',
				    ['support@mail1.nitdgp.ac.in',stud_email],
				    fail_silently=False,
				)
				return HttpResponse(
		                json.dumps({"message": 'Complaint Inserted'}),
		                content_type="application/json"
		            )
	else:
		return HttpResponse(
				json.dumps({"message": 'Not Success !! Something going wrong!!'}),
                content_type="application/json"
			)

@csrf_exempt
def logocompetition(request, **kwarg):
	if request.method == 'POST':		
		#with open(re)
		QueryDict = request.POST
		logovalues = QueryDict.dict()
		print(logovalues)
		qry = Logocomp.objects.filter(email=logovalues['email'])
		if qry:
			return HttpResponse(
                json.dumps({"message": 'Already Register'}),
                content_type="application/json"
            )

		else:
			import os
			img_name = logovalues['email'].split('@')[0]+str(logovalues['mobile'])+'.jpg'
			apsolute_path = 'logocomp/logos/'+img_name
			with open(os.path.join('files/logocomp/logos/',img_name),'wb') as f:
				f.write(request.FILES['logoimg'].read())
			part_name = logovalues['name']
			part_nog = logovalues['guardian']
			part_mobile = logovalues['mobile']
			part_email = logovalues['email']
			logovalues.update({'logoimg': apsolute_path})

			if logovalues:
				Logocomp.objects.create(**logovalues)
			return HttpResponse(
        		json.dumps({"message":'Your Logo Submit Successful !!!'}), 
        		content_type="application/json"
        	)
	else:
		return HttpResponse(
				json.dumps({"message": 'Not Success !! Something going wrong!!'}),
                content_type="application/json"
			)
