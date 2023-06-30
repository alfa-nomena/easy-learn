import pytest
from users.models import User



@pytest.mark.django_db
def test_should_delete_data_in_db(client, url_users, one_user):
    response = client.delete(f"{url_users}{one_user.id}/")
    assert response.status_code == 204
    assert not response.data
    assert not User.objects.filter(pk=one_user.id).exists()
    
@pytest.mark.django_db
def test_should_delete_data_already_deleted_should_fail(client, url_users, one_user):
    pk = one_user.id
    one_user.delete()
    response = client.delete(f"{url_users}{pk}/")
    assert response.status_code == 404
    
@pytest.mark.django_db
def test_should_delete_data_not_in_db_should_fail(client, url_users, Users):
    with Users() as users:
        pk = users.last().id
    response = client.delete(f"{url_users}{pk+1}/")
    assert response.status_code == 404