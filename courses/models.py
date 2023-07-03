from django.db import models

from users.models import User

class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()