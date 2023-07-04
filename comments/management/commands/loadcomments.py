from typing import Any, Optional
from django.core.management.base import BaseCommand
from tqdm import tqdm
from courses.models import Course
from faker import Faker
from users.models import User
from comments.models import Comment
import random




class Command(BaseCommand):
    def clean_db(self):
        for comment in tqdm(Comment.objects.all(), desc='Removing Comments'):
            comment.delete()
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.clean_db()
        faker = Faker()
        for user in tqdm(User.objects.filter(is_superuser=False, is_staff=False, is_active=True), desc='Creating Comments'):
            for course in Course.objects.all():    
                for _ in range(random.randrange(5)):
                    Comment.objects.create(
                        author=user,
                        course=course,
                        content = faker.text(random.randrange(10, 300))
                    )