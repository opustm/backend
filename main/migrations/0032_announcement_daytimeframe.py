# Generated by Django 3.1.2 on 2020-12-04 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_delete_daytimeframe'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayTimeFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('dayschedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daytimeframe', to='main.dayschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.CharField(default='This is a reminder to do your hw', max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_announcement', to='main.event')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamevent', to='main.team')),
            ],
        ),
    ]
