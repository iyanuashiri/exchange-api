from django.db import models

# Create your models here.


class Exchange(models.Model):
    from_currency_code = models.CharField(max_length=10)
    from_currency_name = models.CharField(max_length=100)
    to_currency_code = models.CharField(max_length=10)
    to_currency_name = models.CharField(max_length=100)
    exchange_rate = models.DecimalField(decimal_places=8, max_digits=19)
    last_refreshed = models.DateTimeField()
    timezone = models.CharField(max_length=10)
    bid_price = models.DecimalField(decimal_places=8, max_digits=19)
    ask_price = models.DecimalField(decimal_places=8, max_digits=19)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.from_currency_code} - {self.to_currency_code}'
