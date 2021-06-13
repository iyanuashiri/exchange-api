from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Exchange
from .serializers import ExchangeSerializer
from .alpha import get_foreign_exchange


class ExchangeListCreateView(generics.ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = get_foreign_exchange('BTC', 'USD')
        exchange = Exchange.objects.create(from_currency_code=data['1. From_Currency Code'],
                                           from_currency_name=data['2. From_Currency Name'],
                                           to_currency_code=data['3. To_Currency Code'],
                                           to_currency_name=data['4. To_Currency Name'],
                                           exchange_rate=data['5. Exchange Rate'],
                                           last_refreshed=data['6. Last Refreshed'],
                                           timezone=data['7. Time Zone'],
                                           bid_price=data['8. Bid Price'],
                                           ask_price=data['9. Ask Price'])
        serializer = self.serializer_class(exchange)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
