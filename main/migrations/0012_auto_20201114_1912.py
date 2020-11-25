# Generated by Django 3.1.2 on 2020-11-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201114_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklyavailability',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='weeklyavailability',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='weeklyavailability',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='weeklyavailability',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='weeklyavailability',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='weeklyavailability',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='weeklyavailability',
            name='wednesday',
        ),
        migrations.AddField(
            model_name='weeklyavailability',
            name='available',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.DeleteModel(
            name='DailyAvailability',
        ),
    ]