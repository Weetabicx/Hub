from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import json
import requests 

class SpotifyViewAPI(APIView):

	def post(self, request):
		query = request.data["query"]
		headers = {"Authorization" : f"Bearer {requestToken()}"}
		response = requests.get(f"https://api.spotify.com/v1/search?limit=5&q={query}&type=track&market=GB&offset=0", headers=headers)
		return Response(response.json(), status=status.HTTP_200_OK)




##### Spotify Helper Functions ######
def requestToken():
	with open("config.json") as file:
		data = json.load(file)
		id, secret = data["clientid"], data["clientsecret"]

	request_body = {
		"grant_type": "client_credentials",
		"client_id": id,
		"client_secret": secret
		}

	response = requests.post(f"https://accounts.spotify.com/api/token", data=request_body)


	return response.json()["access_token"]
	
