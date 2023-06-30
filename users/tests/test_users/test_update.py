import pytest 



@pytest.mark.django_db
@pytest.mark.now
def test_update_data_not_in_db_should_fail(client, url_users, Users):
    with Users() as users:
        pk = users.last().id
    response = client.put(f"{url_users}{pk+1}/")
    assert response.status_code == 404

@pytest.mark.django_db
@pytest.mark.now
def test_update_data_already_deleted_should_fail(client, url_users, one_user):
    pk = one_user.id
    one_user.delete()
    response = client.put(f"{url_users}{pk}/")
    assert response.status_code == 404
    
@pytest.mark.django_db
@pytest.mark.now
def test_update_with_no_data_should_fail(client, url_users, one_user):
    response = client.put(f"{url_users}{one_user.id}/")
    assert response.status_code == 400

@pytest.mark.django_db
@pytest.mark.xfail
def test_kjk():
    pass