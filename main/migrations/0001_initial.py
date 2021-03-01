# Generated by Django 3.1.2 on 2021-03-01 06:00

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.UUID('0bc5cc9d-74a0-4deb-9de3-fea2d3449dfc'), editable=False, primary_key=True, serialize=False)),
                ('bio', models.CharField(default='hi there. please call me Steve.', max_length=160)),
                ('picture', models.CharField(default='pic1', max_length=100)),
                ('theme', models.CharField(default='theme1', max_length=100)),
                ('phone', models.CharField(default='123-456-7890', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userSchedule', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('sunday', 'SUNDAY'), ('monday', 'MONDAY'), ('tuesday', 'TUESDAY'), ('wednesday', 'WEDNESDAY'), ('thursday', 'THURSDAY'), ('friday', 'FRIDAY'), ('saturday', 'SATURDAY')], default=('sunday', 'SUNDAY'), max_length=15)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduleTimeFrame', to='main.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('workspace', models.CharField(default='general', max_length=100)),
                ('teamType', models.CharField(choices=[('sub', 'SUB'), ('team', 'TEAM'), ('class', 'CLASS'), ('ensemble', 'ENSEMBLE'), ('club', 'CLUB'), ('social', 'SOCIAL')], default=('sub', 'SUB'), max_length=100)),
                ('picture', models.CharField(default='pic1', max_length=100)),
                ('displayName', models.CharField(default='group', max_length=30)),
                ('description', models.CharField(default='this is an opus team', max_length=100)),
                ('managers', models.ManyToManyField(blank=True, default=[], related_name='teamManagers', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, default=[], related_name='teamMembers', to=settings.AUTH_USER_MODEL)),
                ('owners', models.ManyToManyField(blank=True, default=[], related_name='teamOwners', to=settings.AUTH_USER_MODEL)),
                ('permissions', models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='permissions')),
                ('relatedteams', models.ManyToManyField(blank=True, related_name='_team_relatedteams_+', to='main.Team')),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='Please let me join our group.', max_length=100)),
                ('dateRequested', models.DateTimeField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamRequest', to='main.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userRequest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='Please join our group.', max_length=100)),
                ('inviteeEmail', models.CharField(default='asdf@example.com', max_length=100)),
                ('dateInvited', models.DateTimeField()),
                ('invitee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitee', to=settings.AUTH_USER_MODEL)),
                ('inviter', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamInvitation', to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='event', max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('details', models.CharField(default='This event is blah blah blah..', max_length=100)),
                ('picture', models.CharField(default='pic1', max_length=100)),
                ('invited', models.ManyToManyField(blank=True, related_name='eventInvited', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamEvent', to='main.team')),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userEvent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=1)),
                ('announcement', models.CharField(default='"Do your hw" -management', max_length=280)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('acknowledged', models.ManyToManyField(blank=True, related_name='userAnnouncementAcknowledgment', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creatorAnnouncement', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventAnnouncement', to='main.event')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamAnnouncement', to='main.team')),
            ],
        ),
    ]
