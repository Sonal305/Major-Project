# Generated by Django 3.1.3 on 2021-02-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_creditscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='creditScore',
            field=models.FloatField(default=100000),
        ),
    ]