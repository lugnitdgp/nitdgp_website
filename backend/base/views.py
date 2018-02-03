from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from department.models import Department

dept_ids = {}

for dept in Department.objects.all():
    dept_ids[dept.short_code] = dept.id


class APIRoot(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        resp_dict = {
            'dashboard': reverse('dashboard:list-tile-content', request=request),
            'department': reverse('department:list-department', request=request),
            'about_us': {},
            'hod': {},
        }

        for dept_id in dept_ids:
            resp_dict['about_us'][dept_id] = reverse('department:retrieve-department-about', request=request, kwargs={'id': dept_ids[dept_id]})
            resp_dict['hod'][dept_id] = reverse('department:retrieve-department-hod', request=request, kwargs={'id': dept_ids[dept_id]})

        return Response(resp_dict)
