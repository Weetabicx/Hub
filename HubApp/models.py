from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class User(AbstractUser):

    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
    rank = models.IntegerField(default=2)

    def __str__(self) -> str:
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return  {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }