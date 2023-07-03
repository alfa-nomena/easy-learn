import pytest
from users.models import User




@pytest.mark.django_db
def test_update_data_not_in_db_should_fail(client, url_users, Users):
    with Users() as users:
        pk = users.last().id
    response = client.put(f"{url_users}{pk+1}/")
    assert response.status_code == 404

@pytest.mark.django_db
def test_update_data_already_deleted_should_fail(client, url_users, one_user):
    pk = one_user.id
    one_user.delete()
    response = client.put(f"{url_users}{pk}/")
    assert response.status_code == 404
    
@pytest.mark.django_db
def test_update_with_no_data_should_fail(client, url_users, one_user):
    response = client.put(f"{url_users}{one_user.id}/")
    assert response.status_code == 400

@pytest.mark.django_db
def test_update_should_edit_in_the_database(client, url_users, one_user, faker):
    while True:
        username = faker.user_name()
        if not User.objects.filter(username=username).exists():
            break
        
    data = {
        'username': username,
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
    }
    response = client.patch(f"{url_users}{one_user.id}/", data=data)
    edited_data = response.data
    one_user.refresh_from_db()
    
    assert response.status_code == 200
    assert one_user.id == edited_data['id']
    assert one_user.username == edited_data['username'] == data['username']
    assert one_user.first_name == edited_data['first_name']  == data['first_name']
    assert one_user.last_name == edited_data['last_name'] == data['last_name']
    assert one_user.email == edited_data['email'] == data['email']