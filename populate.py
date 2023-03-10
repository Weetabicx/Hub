import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hub.settings")
import django
django.setup()

from HubApp.models import User
from uuid import uuid4

def create_user(username, password, firstname, lastname, email, is_superuser=False, is_staff=False, rank=2, costing=False):
    # print(username, password, firstname, lastname, email, is_superuser, is_staff, rank, costing, spotify)
    user = User.objects.create(id=uuid4(), username=username,first_name=firstname, last_name=lastname, email=email, is_superuser=is_superuser, is_staff=is_staff, rank=rank, costing=costing)
    user.set_password(password)
    user.save()

create_user("John", "Wrestlemania", "John", "Cena", "JohnCena@outlook.com")