from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    pass


    def __str__(self):
        return self.username
