from django.urls import reverse

import pytest


@pytest.mark.django_db
def test_exchange_list_reverse(authenticated):
    client = authenticated
    url = reverse('exchanges:exchange-list-create')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_exchange_list_url(authenticated):
    client = authenticated
    url = '/api/v1/quotes/'
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_exchange_create_reverse(authenticated):
    client = authenticated
    url = reverse('exchanges:exchange-list-create')
    response = client.post(url)
    assert response.status_code == 201


@pytest.mark.django_db
def test_exchange_create_url(authenticated):
    client = authenticated
    url = '/api/v1/quotes/'
    response = client.post(url)
    assert response.status_code == 201
