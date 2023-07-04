from django.db import models
from courses.models import Course
from users.models import User



class Comment(models.Model):
    date_posted = models.DateField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)