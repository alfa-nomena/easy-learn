import contextlib
import pytest
from users.models import User
import random
from faker import Faker


@pytest.fixture
def url_users():
    return '/api/users/'

@pytest.fixture
def one_user(Users):
    with Users() as users:
        yield random.choice(users)
