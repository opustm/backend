# Generated by Django 3.1.2 on 2021-03-30 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_auto_20210330_0915"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userEvent",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userRequest",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
