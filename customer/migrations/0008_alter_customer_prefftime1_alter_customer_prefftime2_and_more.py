# Generated by Django 4.0.3 on 2022-03-27 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_customer_prefftime1_alter_customer_prefftime2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='prefftime1',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 23, 32, 19, 685515), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime2',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 23, 32, 19, 685528), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime3',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 23, 32, 19, 685537), null=True),
        ),
    ]
