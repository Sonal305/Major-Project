# Generated by Django 3.1.3 on 2021-01-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='publicAddress',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
