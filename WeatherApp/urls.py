from django.urls import path
from WeatherApp.views import (
    WeatherViewApi
)

urlpatterns = [
    path('', WeatherViewApi.as_view()),
]

