# Generated by Django 3.2.3 on 2023-07-28 20:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptproject', '0004_bookingsession_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingsession',
            name='age',
            field=models.IntegerField(default='18', validators=[django.core.validators.MinValueValidator(18)]),
        ),
    ]
