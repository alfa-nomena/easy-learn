from typing import Any, Optional
from django.core.management.base import BaseCommand
from tqdm import tqdm
from courses.models import Course
from faker import Faker
from users.models import User
import random




class Command(BaseCommand):
    def clean_db(self):
        for course in tqdm(Course.objects.all(), desc='Removing Courses'):
            course.delete()
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.clean_db()
        faker = Faker()
        for user in tqdm(User.objects.filter(is_superuser=False, is_staff=False, is_active=True), desc='Creating courses'):
            for _ in range(random.randrange(0,10)):
                Course.objects.create(
                    owner=user,
                    title = faker.text(100),
                    content = faker.text(1000)
                )