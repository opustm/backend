# Generated by Django 3.1.2 on 2021-03-30 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_auto_20210330_0855"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teamRequest",
                to="main.team",
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
