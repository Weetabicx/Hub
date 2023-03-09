from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import json
import requests 

class WeatherViewApi(APIView):

    def get(self, request):
        permission_classes = (permissions.IsAuthenticated,)
        with open('config.json') as file:
            data = json.load(file)
        
        key, code = data['weatherAPIKey'], data['code']
        r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={code}&aqi=no')
        return Response(r.json(), status=status.HTTP_200_OK)