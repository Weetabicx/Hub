from django.urls import path
from SpotifyApp.views import *

urlpatterns = [
    path('', SpotifyViewAPI.as_view()),
]

