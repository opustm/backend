# Generated by Django 3.1.2 on 2020-12-05 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_opusclique'),
    ]

    operations = [
        migrations.AddField(
            model_name='opusclique',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cliquesTeam', to='main.opusteam'),
            preserve_default=False,
        ),
    ]
