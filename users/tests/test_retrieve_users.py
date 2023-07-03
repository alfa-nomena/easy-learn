import pytest


@pytest.mark.django_db
def test_retrieve_all_should_return_empty_list_if_no_data_in_db(client, url_users):
    response = client.get(url_users)
    assert response.status_code == 200
    assert response.data == []

@pytest.mark.django_db
def test_retrieve_all_should_return_all_data_in_db(client, url_users, Users):
    with Users() as users:
        response = client.get(url_users)
        datas = response.data
        
        assert response.status_code == 200
        assert len(datas) == len(users)
        for user, data in zip(users, datas):
            assert data['id'] == user.id
            assert data['username'] == user.username
            assert data['first_name'] == user.first_name
            assert data['last_name'] == user.last_name
            assert data['email'] == user.email
            assert data['is_staff'] == user.is_staff
            assert data['is_superuser'] == user.is_superuser
            assert data['is_active'] == user.is_active

@pytest.mark.django_db
def test_retrieve_one_by_pk_that_is_in_database_should_succeed(client, url_users, one_user):
    response = client.get(f"{url_users}{one_user.id}/")
    data = response.data
    
    assert response.status_code == 200
    assert data['id'] == one_user.id
    assert data['username'] == one_user.username
    assert data['first_name'] == one_user.first_name
    assert data['last_name'] == one_user.last_name
    assert data['email'] == one_user.email
    assert data['is_staff'] == one_user.is_staff
    assert data['is_superuser'] == one_user.is_superuser
    assert data['is_active'] == one_user.is_active
    
    
@pytest.mark.django_db
def test_retrieve_one_by_pk_that_is_not_in_database_should_fail(client, url_users, Users):
    with Users() as users:
        pk = users.last().id
    response = client.get(f"{url_users}{pk+1}/")
    assert response.status_code == 404
    
@pytest.mark.django_db
def test_retrieve_one_by_pk_that_is_already_deleted_should_fail(client, url_users, one_user):
    pk = one_user.id
    one_user.delete()
    response = client.get(f"{url_users}{pk}/")
    assert response.status_code == 404