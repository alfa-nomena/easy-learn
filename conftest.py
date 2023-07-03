import contextlib
import random
import pytest
from rest_framework.test import APIClient
from faker import Faker

from users.models import User


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def faker():
    return Faker()

@pytest.fixture(scope="function")
@pytest.mark.django_db
def Users(faker):
    class UsersData:
        def __enter__(self):
            for _ in range(random.randrange(10,40)):
                random_or_none = lambda x : x if random.choice([True, False]) else ''
                User.objects.create(
                    username=faker.user_name(),
                    password='password',
                    email = random_or_none(faker.email()) ,
                    first_name = random_or_none(faker.first_name()),
                    last_name = random_or_none(faker.last_name())
                )
            self.users = User.objects.all()
            print("Creating users")
            return self.users

        def __exit__(self, *args, **kwargs):
            for user in self.users:
                with contextlib.suppress(Exception):
                    user.delete()
            print("Clearing users")
    return UsersData