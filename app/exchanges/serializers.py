from rest_framework import serializers

from .models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exchange
        fields = ('from_currency_code', 'from_currency_name', 'to_currency_code', 'to_currency_name', 'exchange_rate',
                  'last_refreshed', 'timezone', 'bid_price', 'ask_price')