# Generated by Django 3.1.2 on 2020-11-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201114_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyavailability',
            name='available',
            field=models.BooleanField(null=True),
        ),
    ]
