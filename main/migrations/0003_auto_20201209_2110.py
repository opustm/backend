# Generated by Django 3.1.2 on 2020-12-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201207_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clique',
            name='parents',
        ),
        migrations.AddField(
            model_name='clique',
            name='relatedCliques',
            field=models.ManyToManyField(blank=True, related_name='_clique_relatedCliques_+', to='main.Clique'),
        ),
    ]