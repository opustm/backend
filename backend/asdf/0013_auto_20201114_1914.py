# Generated by Django 3.1.2 on 2020-11-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201114_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyavailability',
            name='week',
            field=models.DateTimeField(),
        ),
    ]