# Generated by Django 3.0.7 on 2020-06-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organigramme', '0011_auto_20200619_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='fonction',
            name='groupe',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
