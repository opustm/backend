# Generated by Django 3.1.2 on 2020-12-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20201204_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announcement',
            field=models.CharField(default='"Do your hw" -management', max_length=100),
        ),
    ]