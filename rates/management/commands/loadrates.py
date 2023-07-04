from typing import Any, Optional
from django.core.management.base import BaseCommand
from tqdm import tqdm
from courses.models import Course
from faker import Faker
from users.models import User
import random
from rates.models import Rate




class Command(BaseCommand):
    def clean_db(self):
        for rate in tqdm(Rate.objects.all(), desc='Removing Rates'):
            rate.delete()
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.clean_db()
        faker = Faker()
        for course in tqdm(Course.objects.all(), desc='Creating Comments'):
            for user in User.objects.filter(is_superuser=False, is_staff=False, is_active=True).order_by('?'):
                if bool(random.getrandbits(1)):
                    Rate.objects.create(
                        author=user,
                        course=course,
                        value=random.randrange(6)
                    )