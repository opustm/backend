# Generated by Django 3.1.2 on 2021-02-18 16:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamType',
            field=models.CharField(choices=[('sub', 'SUB'), ('team', 'TEAM'), ('class', 'CLASS'), ('ensemble', 'ENSEMBLE'), ('club', 'CLUB'), ('social', 'SOCIAL')], default=('sub', 'SUB'), max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('83776bda-d5e2-41a3-8061-2e281149aa13'), editable=False, primary_key=True, serialize=False),
        ),
    ]