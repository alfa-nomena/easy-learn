import pytest



@pytest.mark.django_db
def test_register_user_with_no_data_should_fail(client, url_users):
    response = client.post(url_users)
    data = response.data
    assert response.status_code == 400

@pytest.mark.django_db
def test_register_user_with_no_password_should_fail(client, url_users):
    user = {
        "username": 'test'
    }
    response = client.post(url_users, user)
    data = response.data
    assert response.status_code == 400

@pytest.mark.django_db
def test_register_user_with_no_username_should_fail(client, url_users):
    user = {
        "password": 'test'
    }
    response = client.post(url_users, user)
    data = response.data
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_user_with_username_and_password_should_suceed(client, url_users):
    data = {
        "username": 'test',
        "password": 'test'
    }
    response = client.post(url_users, data)
    user = response.data
    assert response.status_code == 201
    assert user['username'] == data['username']
    assert user['email'] == ''
    assert user['first_name'] == ''
    assert user['last_name'] == ''
    assert user['is_staff'] == False
    assert user['is_superuser'] == False
