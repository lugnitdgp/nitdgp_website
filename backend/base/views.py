from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRoot(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        resp_dict = {
            'dashboard': reverse('dashboard:list-tile-content', request=request),
            'department': reverse('department:list-department', request=request),
        }

        return Response(resp_dict)
