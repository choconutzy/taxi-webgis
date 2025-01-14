# Generated by Django 5.1.4 on 2024-12-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxiModel',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('vendor_id', models.CharField(max_length=256)),
                ('pickup_datetime', models.DateTimeField()),
                ('dropoff_datetime', models.DateTimeField()),
                ('passenger_count', models.IntegerField()),
                ('trip_distance', models.FloatField(default=0.0, max_length=256)),
                ('pickup_longitude', models.FloatField(default=0.0, max_length=256)),
                ('pickup_latitude', models.FloatField(default=0.0, max_length=256)),
                ('store_and_fwd_flag', models.CharField(max_length=5)),
                ('dropoff_longitude', models.FloatField(default=0.0, max_length=256)),
                ('dropoff_latitude', models.FloatField(default=0.0, max_length=256)),
                ('payment_type', models.CharField(max_length=5)),
                ('fare_amount', models.FloatField(default=0.0, max_length=256)),
                ('mta_tax', models.FloatField(default=0.0, max_length=256)),
                ('tip_amount', models.FloatField(default=0.0, max_length=256)),
                ('tolls_amount', models.FloatField(default=0.0, max_length=256)),
                ('total_amount', models.FloatField(default=0.0, max_length=256)),
                ('imp_surcharge', models.FloatField(default=0.0, max_length=256)),
                ('extra', models.CharField(default=0.0, max_length=256)),
                ('rate_code', models.IntegerField()),
            ],
            options={
                'db_table': 'taxi',
            },
        ),
    ]
