# Generated by Django 4.2.7 on 2023-11-14 06:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptproject', '0009_bookingrequest_delete_bookingsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Messages',
                'ordering': ['created_on'],
            },
        ),
        migrations.RemoveField(
            model_name='bookingrequest',
            name='status',
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='phonenumber',
            field=models.CharField(default='1234567890', max_length=15),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='age',
            field=models.IntegerField(default='0', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='email',
            field=models.EmailField(default='your@mail.com', max_length=70),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='message',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='name',
            field=models.CharField(default='State your name', max_length=100),
        ),
    ]
