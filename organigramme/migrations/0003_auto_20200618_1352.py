# Generated by Django 3.0.7 on 2020-06-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organigramme', '0002_auto_20200618_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='fax',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='telephone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
