# Generated by Django 3.1.2 on 2021-02-23 01:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210221_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='invited',
        ),
        migrations.RemoveField(
            model_name='event',
            name='notGoing',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a2b61717-e600-4d13-9f17-435df7a2fcdc'), editable=False, primary_key=True, serialize=False),
        ),
    ]
