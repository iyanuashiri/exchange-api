from datetime import datetime

import pytest


@pytest.mark.django_db
def test_account_model(account):
    assert account.email == 'iyanuajao@gmail.com'
    assert account.is_active is True
    assert account.is_staff is False
    # assert account.date_joined == datetime.now()


@pytest.mark.django_db
def test_account_field_label(account):
    assert account._meta.get_field('email').verbose_name == 'email address'
    assert account._meta.get_field('is_active').verbose_name == 'active'
    assert account._meta.get_field('is_staff').verbose_name == 'staff status'
    assert account._meta.get_field('date_joined').verbose_name == 'date joined'
