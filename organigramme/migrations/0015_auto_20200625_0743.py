# Generated by Django 3.0.7 on 2020-06-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organigramme', '0014_auto_20200624_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='fonction',
            name='groupe',
        ),
    ]
