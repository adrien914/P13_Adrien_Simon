# Generated by Django 3.0.7 on 2020-06-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organigramme', '0013_auto_20200619_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
