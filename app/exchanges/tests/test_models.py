import pytest


@pytest.mark.django_db
def test_exchange_model(exchange):
    assert exchange.from_currency_code == 'BTC'
    assert exchange.from_currency_name == 'Bitcoin'
    assert exchange.to_currency_code == 'USD'
    assert exchange.to_currency_name == 'United States Dollar'
    assert exchange.exchange_rate == '35894.79000000'
    assert exchange.last_refreshed == '2021-06-12T13:28:01Z'
    assert exchange.timezone == 'UTC'
    assert exchange.bid_price == '35894.79000000'
    assert exchange.ask_price == '35894.80000000'


@pytest.mark.django_db
def test_exchange_field_label(exchange):
    assert exchange._meta.get_field('from_currency_code').verbose_name == 'from currency code'
    assert exchange._meta.get_field('from_currency_name').verbose_name == 'from currency name'
    assert exchange._meta.get_field('to_currency_code').verbose_name == 'to currency code'
    assert exchange._meta.get_field('to_currency_name').verbose_name == 'to currency name'
    assert exchange._meta.get_field('exchange_rate').verbose_name == 'exchange rate'
    assert exchange._meta.get_field('last_refreshed').verbose_name == 'last refreshed'
    assert exchange._meta.get_field('timezone').verbose_name == 'timezone'
    assert exchange._meta.get_field('bid_price').verbose_name == 'bid price'
    assert exchange._meta.get_field('ask_price').verbose_name == 'ask price'


@pytest.mark.django_db
def test_exchange_field_attributes(exchange):
    assert exchange._meta.get_field('from_currency_code').max_length == 10
    assert exchange._meta.get_field('from_currency_name').max_length == 100
    assert exchange._meta.get_field('to_currency_code').max_length == 10
    assert exchange._meta.get_field('to_currency_name').max_length == 100
    assert exchange._meta.get_field('timezone').max_length == 10