from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.

class WeatherViewApi(APIView):

    def get(self, request):
        permission_classes = (permissions.IsAuthenticated,)
        return Response(request.data, status=status.HTTP_200_OK)