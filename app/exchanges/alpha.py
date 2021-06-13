from alpha_vantage.foreignexchange import ForeignExchange

from exchange_api.settings import ALPHAVANTAGE_ACCESS_KEY

fx = ForeignExchange(key=ALPHAVANTAGE_ACCESS_KEY)


def get_foreign_exchange(from_currency, to_currency):
    response, _ = fx.get_currency_exchange_rate(from_currency=from_currency, to_currency=to_currency)
    return response
