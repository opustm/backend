# Generated by Django 3.1.2 on 2020-12-07 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_todo_todolist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='toDoList',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userToDo', to='main.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
