# Generated by Django 3.1.3 on 2021-01-31 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20210131_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentagency',
            name='publicAddress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
