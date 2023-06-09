from typing import Any, Optional
from django.core.management.base import BaseCommand
from users.models import User
from faker import Faker
import random
from tqdm import tqdm

class Command(BaseCommand):
    def clean_db(self):
        for user in tqdm(User.objects.all(), desc='Removing users from DB'):
            user.delete()
    
    def handle(self, *args, **kwargs) -> str | None:
        self.clean_db()
        faker = Faker()
        for i in tqdm(range(random.randrange(50, 150)), desc='Creating users'):
            random_or_none = lambda x : x if bool(random.getrandbits(1)) else ''
            User.objects.create(
                username=faker.user_name(),
                password='password',
                email = random_or_none(faker.email()) ,
                first_name = random_or_none(faker.first_name()),
                last_name = random_or_none(faker.last_name()), 
                is_staff=i<10,
                is_active=bool(random.getrandbits(1))
            )