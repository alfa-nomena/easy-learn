from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.username}"