# Generated by Django 3.1.3 on 2021-02-02 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0004_shipmentagency_publicaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentorder',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recievers', to=settings.AUTH_USER_MODEL),
        ),
    ]