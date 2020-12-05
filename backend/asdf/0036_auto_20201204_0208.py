# Generated by Django 3.1.2 on 2020-12-04 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20201204_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayschedule',
            name='team',
        ),
        migrations.AddField(
            model_name='dayschedule',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='weekscheduleuser', to='main.team'),
        ),
    ]