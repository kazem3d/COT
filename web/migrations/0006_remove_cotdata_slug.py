# Generated by Django 3.0.7 on 2020-06-05 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_currency_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotdata',
            name='slug',
        ),
    ]
