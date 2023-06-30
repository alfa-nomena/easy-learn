import contextlib
import pytest
from users.models import User
import random
from faker import Faker


@pytest.fixture
def url_users():
    return '/users/users/'


@pytest.fixture
@pytest.mark.django_db
def Users():






    class UsersData:
        def __enter__(self):
            faker = Faker()
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

@pytest.fixture
def one_user(Users):
    with Users() as users:
        yield random.choice(users)
