# Generated by Django 3.1.2 on 2021-03-30 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="team",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teamRequest",
                to="main.team",
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userRequest",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
