# Generated by Django 3.1.3 on 2021-02-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_publicaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]