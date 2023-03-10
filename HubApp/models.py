from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class User(AbstractUser):

    id = models.CharField(max_length=36, unique=True, primary_key=True)
    bio = models.CharField(max_length=1024, blank=True, default="")
    rank = models.IntegerField(default=2)
    costing = models.BooleanField(default=False)
    spotify = models.CharField(max_length=255, blank=True, default="")

    def __str__(self) -> str:
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return  {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        } 