from django.urls import reverse

from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
def test_account_create_reverse():
    client = APIClient()
    url = reverse('accounts:auth-create')
    response = client.post(url, data={"password": "decagon1234", "email": "iyanu@example.com"})
    assert response.status_code == 201
    assert response.data['id'] == 1
    assert response.data['email'] == 'iyanu@example.com'


@pytest.mark.django_db
def test_account_create_url():
    client = APIClient()
    url = '/api/v1/auth/users/'
    response = client.post(url, data={"password": "decagon1234", "email": "iyanu@example.com"})
    assert response.status_code == 201
    assert response.data['id'] == 1
    assert response.data['email'] == 'iyanu@example.com'
