from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Account


class AccountCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": _("Can't create account")
    }

    class Meta:
        model = Account
        fields = ('id', 'email', 'password')

    def validate(self, attrs):
        user = Account(attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )
        return attrs

    def create(self, validated_data):
        try:
            account = Account.objects.create_user(**validated_data)

        except IntegrityError:
            self.fail("cannot_create_user")
        account.save()
        return account


class TokenCreateSerializer(serializers.Serializer):
    password = serializers.CharField(required=False, style={"input_type": "password"})

    default_error_messages = {
        "invalid_credentials": _("Cannot log in with provided credentials"),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account = None
        self.fields['email'] = serializers.CharField(required=False)

    def validate(self, attrs):
        password = attrs.get("password")
        params = {"email": attrs.get("email")}
        self.account = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.account:
            self.account = Account.objects.filter(**params).first()
            if self.account and not self.account.check_password(password):
                self.fail("invalid_credentials")
        if self.account and self.account.is_active:
            return attrs
        self.fail("invalid_credentials")


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ('auth_token',)
