import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, GroupManager
from django.utils.translation import gettext_lazy as _
from django.db.models.fields import BooleanField
from django.db.models.fields import related
from datetime import datetime

class AbstractGroup(models.Model):
    """
    Groups are a generic way of categorizing users to apply permissions, or
    some other label, to those users. A user can belong to any number of
    groups.
    A user in a group automatically has all the permissions granted to that
    group. For example, if the group 'Site editors' has the permission
    can_edit_home_page, any user in that group will have that permission.
    Beyond permissions, groups are a convenient way to categorize users to
    apply some label, or extended functionality, to them. For example, you
    could create a group 'Special users', and you could write code that would
    do special things to those users -- such as giving them access to a
    members-only portion of your site, or sending them members-only email
    messages.
    """
    name = models.CharField(_('name'), max_length=150, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissions'),
        blank=True,
    )

    objects = GroupManager()

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        abstract = True

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    bio = models.CharField(max_length=160, default='hi there. please call me Steve.')
    picture = models.CharField(max_length=100, default='pic1')
    theme = models.CharField(max_length=100, default='theme1')
    phone = models.CharField(max_length=100, default='123-456-7890')
    def usercode(self):
        return f'{self.username}'


class Team(AbstractGroup):
    workspace = models.CharField(max_length=100, default="general")
    teamType = models.CharField(max_length=100, choices=[("sub", "SUB"),("team","TEAM"), ("class","CLASS"), ("ensemble", "ENSEMBLE"), ("club", "CLUB"), ("social", "SOCIAL")], default=("sub", "SUB"))
    relatedteams = models.ManyToManyField("self", blank=True)
    picture = models.CharField(max_length=100, default='pic1')
    displayName = models.CharField(max_length=30, default='group')
    members = models.ManyToManyField(User, related_name='teamMembers', default=[], blank=True)
    managers = models.ManyToManyField(User, related_name='teamManagers', default=[], blank=True)
    owners = models.ManyToManyField(User, related_name='teamOwners', default=[], blank=True)

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')
    def __str__(self):
        return f'{self.name}'

class Invitation(models.Model):#will need to delete each row once invitee_email joins team
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamInvitation')
    invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitee', blank=True)
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviter', blank=True)
    message = models.CharField(max_length=100, default='Please join our group.')
    inviteeEmail=models.CharField(max_length=100, default='asdf@example.com')
    dateInvited=models.DateTimeField()
    
    def __str__(self):
        return '{} invited to {} by {}'.format(self.inviteeEmail, self.team, self.inviter)

class Event(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamEvent', blank=True, null=True)#ONE TEAM CAN HAVE MANY EVENTS (ONE2M)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userEvent', blank=True, null=True)#ONE USER CAN HAVE MANY EVENTS (ONE2M)
    name = models.CharField(max_length=100, default='event')
    start = models.DateTimeField()
    end = models.DateTimeField()
    invited = models.ManyToManyField(User, related_name='eventInvited', blank=True)
    notGoing = models.ManyToManyField(User, related_name='notGoing', blank=True)
    details = models.CharField(max_length=100, default='This event is blah blah blah..')
    picture = models.CharField(max_length=100, default='pic1')
    def __str__(self):
        return f"{self.name} made by {self.user}."

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userSchedule')
    def __str__(self):
        return f'{self.user} schedule'

class TimeFrame(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='scheduleTimeFrame')
    weekday = models.CharField(max_length=15, choices=[("sunday","SUNDAY"), ("monday","MONDAY"), ("tuesday","TUESDAY"), ("wednesday","WEDNESDAY"), ("thursday","THURSDAY"), ("friday","FRIDAY"), ("saturday","SATURDAY")], default=("sunday","SUNDAY"))
    start = models.TimeField()
    end = models.TimeField()
    def __str__(self):
        return f'TimeFrame for {self.schedule} Available from {self.start} to {self.end} on {self.weekday}.'

class Announcement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamAnnouncement')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventAnnouncement', blank=True, null=True)
    creator = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='creatorAnnouncement')
    priority = models.IntegerField(default=1)
    announcement = models.CharField(max_length=280, default='\"Do your hw\" -management')
    end = models.DateTimeField(blank=True, null=True)
    acknowledged = models.ManyToManyField(User, related_name='userAnnouncementAcknowledgment')
    def __str__(self):
        return f'{self.team}: {self.announcement} with event {self.event}.'

class Reaction(models.Model):
    reactor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userReactor')
    reaction = models.CharField(max_length=100, choices=[("thumbs up", "THUMBS UP"),("dislike","DISLIKE")],  default=("dislike", "DISLIKE"))

class DirectMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userSenderDM')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userRecipientDM')
    message = models.CharField(max_length=500, default='message text')
    sentAt = models.DateTimeField()
    reaction = models.ManyToManyField(Reaction, related_name='directMessageReaction')

class TeamMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userSenderCM')
    recipient = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamRecipientCM')
    message = models.CharField(max_length=500, default='message text')
    sentAt = models.DateTimeField()
    reaction = models.ManyToManyField(Reaction, related_name='teamMessageReaction')

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userToDo')
    name = models.CharField(max_length=100, default='laundry')
    due = models.DateTimeField()

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userRequest')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamRequest')
    message = models.CharField(max_length=100, default='Please let me join our group.')
    dateRequested = models.DateTimeField()