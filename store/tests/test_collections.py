from rest_framework.test import APIClient
import pytest   
from rest_framework import status

@pytest.mark.django_db
class TestUserAuthentication:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.post('/store/collections/', { 'title': 'a' })
      
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_returns_403(self,api_client):
        api_client.force_authenticate(user={})
        response = api_client.post('/store/collections/', { 'title': 'a' })
      
        assert response.status_code == status.HTTP_403_FORBIDDEN