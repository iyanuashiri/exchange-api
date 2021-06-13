from pytest_factoryboy import register
import pytest
from rest_framework.test import APIClient

from accounts.factories import AccountFactory
from exchanges.factories import ExchangeFactory

register(AccountFactory, 'account')
register(ExchangeFactory, 'exchange')


@pytest.fixture
def authenticated():
    client = APIClient()
    client.post('/api/v1/auth/users/', data={"email": "iyanu@example.com",
                                                                  "password": "decagon1234"})

    response = client.post('/api/v1/auth/token/login/', data={"password": "decagon1234",
                                                                                   "email": "iyanu@example.com"})
    auth_token = response.data['auth_token']
    client.credentials(HTTP_AUTHORIZATION='Token ' + auth_token)
    return client
