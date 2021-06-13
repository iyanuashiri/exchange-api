from django.contrib.auth import login, user_logged_in

from rest_framework.authtoken.models import Token


def login_user(request, user):
    token, _ = Token.objects.get_or_create(user=user)
    login(request, user)
    user_logged_in.send(sender=user.__class__, request=request, user=user)
    return token


class ActionViewMixin:
    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self._action(serializer)