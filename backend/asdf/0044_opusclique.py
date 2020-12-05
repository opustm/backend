# Generated by Django 3.1.2 on 2020-12-05 18:12

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0043_auto_20201205_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpusClique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('picture', models.CharField(default='pic1', max_length=100)),
                ('permissions', models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='permissions')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'abstract': False,
                'swappable': 'AUTH_OPUSCLIQUE_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
