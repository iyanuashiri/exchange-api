from factory.django import DjangoModelFactory

from .models import Exchange


class ExchangeFactory(DjangoModelFactory):
    class Meta:
        model = Exchange

    from_currency_code = 'BTC'
    from_currency_name = 'Bitcoin'
    to_currency_code = 'USD'
    to_currency_name = 'United States Dollar'
    exchange_rate = '35894.79000000'
    last_refreshed = '2021-06-12T13:28:01Z'
    timezone = 'UTC'
    bid_price = '35894.79000000'
    ask_price = '35894.80000000'
