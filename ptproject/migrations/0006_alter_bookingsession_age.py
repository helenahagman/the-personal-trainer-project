# Generated by Django 3.2.3 on 2023-07-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptproject', '0005_alter_bookingsession_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingsession',
            name='age',
            field=models.CharField(default='min18years', max_length=20),
        ),
    ]
