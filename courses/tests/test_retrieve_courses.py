import pytest
from users.models import User
from courses.models import Course


@pytest.mark.django_db
@pytest.mark.now
def test_retrieve_all_should_return_all_data_in_db(client, url_courses, Courses):
    with Courses() as courses:
        response = client.get(url_courses)
        datas = response.data
        print(courses)
        return None
        assert response.status_code == 200
        assert len(datas) == len(courses)
        for course, data in zip(courses, datas):
            assert data['id'] == course.id
            assert data['title'] == course.title
            assert data['content'] == course.content
            assert data['owner'] == course.owner
            print()
            print(data, course)
            print()