from django.db import models
from django.contrib.auth.models import AbstractUser

# User Models
class User(AbstractUser):
    pass

# Base model class for model
class BaseModel(models.Model):
    activate = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
