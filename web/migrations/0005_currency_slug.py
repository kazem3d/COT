# Generated by Django 3.0.7 on 2020-06-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_cotdata_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
