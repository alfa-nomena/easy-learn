import contextlib
import random

import pytest
from courses.models import Course

from users.models import User


@pytest.fixture
@pytest.mark.django_db
def Courses(faker, Users):
    class CoursesData:
        def __enter__(self):
            with Users() as _:
                for user in User.objects.filter(is_superuser=False, is_staff=False, is_active=True):
                    for _ in range(random.randrange(0,10)):
                        Course.objects.create(
                            owner=user,
                            title = faker.text(100),
                            content = faker.text(1000)
                        )
                print("Creating courses")
                yield Course.objects.all()

        def __exit__(self, *args, **kwargs):
            print("Clearing courses")
    return CoursesData

@pytest.fixture
def url_courses():
    return '/api/courses/'