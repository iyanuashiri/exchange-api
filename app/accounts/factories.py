from datetime import datetime

from factory.django import DjangoModelFactory
import factory

from .models import Account


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    email = 'iyanuajao@gmail.com'
    date_joined = factory.LazyFunction(datetime.now)
    is_staff = False
    is_active = True
