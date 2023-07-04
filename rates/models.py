from django.db import models
from courses.models import Course
from users.models import User





class Rate(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(choices=[(i, i) for i in range(6)], default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        unique_together = [['author', 'course']]