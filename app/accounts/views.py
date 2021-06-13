from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import AccountCreateSerializer, TokenSerializer, TokenCreateSerializer
from .models import Account
from .utils import ActionViewMixin, login_user


# Create your views here.


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    permission_classes = (permissions.AllowAny,)


class TokenCreateView(ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to obtain user authentication token.
    """

    serializer_class = TokenCreateSerializer
    permission_classes = (permissions.AllowAny,)

    def _action(self, serializer):
        token = login_user(self.request, serializer.account)
        token_serializer_class = TokenSerializer
        return Response(
            data=token_serializer_class(token).data, status=status.HTTP_200_OK
        )