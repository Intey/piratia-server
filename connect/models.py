from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    level = models.PositiveIntegerField(default=1)
