# Generated by Django 3.0.7 on 2020-08-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organigramme', '0017_groupe_importance'),
    ]

    operations = [
        migrations.AddField(
            model_name='pole',
            name='classement',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
