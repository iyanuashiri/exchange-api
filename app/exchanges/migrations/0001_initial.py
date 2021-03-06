# Generated by Django 3.2.4 on 2021-06-12 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency_code', models.CharField(max_length=10)),
                ('from_currency_name', models.CharField(max_length=100)),
                ('to_currency_code', models.CharField(max_length=10)),
                ('to_currency_name', models.CharField(max_length=100)),
                ('exchange_rate', models.DecimalField(decimal_places=8, max_digits=19)),
                ('last_refreshed', models.DateTimeField()),
                ('timezone', models.CharField(max_length=10)),
                ('bid_price', models.DecimalField(decimal_places=8, max_digits=19)),
                ('ask_price', models.DecimalField(decimal_places=8, max_digits=19)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
