# Generated by Django 3.2.3 on 2023-07-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptproject', '0006_alter_bookingsession_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingsession',
            name='age',
            field=models.CharField(default='18', max_length=2),
        ),
    ]