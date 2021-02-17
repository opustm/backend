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
        abstract = True#way to making abstract class! :O

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


class Clique(AbstractGroup):
    workspace = models.CharField(max_length=100, default="general")
    cliqueType = models.CharField(max_length=100, choices=[("sub", "SUB"),("team","Team"), ("class","CLASS"), ("ensemble", "ENSEMBLE"), ("club", "CLUB"), ("social", "SOCIAL")], default=("sub", "SUB"))
    relatedCliques = models.ManyToManyField("self", blank=True)
    picture = models.CharField(max_length=100, default='pic1')
    displayName = models.CharField(max_length=30, default='group')
    members = models.ManyToManyField(User, related_name='teamMembers', default=[])
    managers = models.ManyToManyField(User, related_name='teamManagers', default=[])
    owners = models.ManyToManyField(User, related_name='teamOwners', default=[])

    class Meta:
        verbose_name = _('clique')
        verbose_name_plural = _('cliques')
    def __str__(self):
        return f'{self.name}'

class Invitation(models.Model):#will need to delete each row once invitee_email joins team
    clique = models.ForeignKey(Clique, on_delete=models.CASCADE, related_name='cliqueInvitation')
    invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitee', blank=True)
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviter', blank=True)
    message = models.CharField(max_length=100, default='Please join our group.')
    inviteeEmail=models.CharField(max_length=100, default='asdf@example.com')
    dateInvited=models.DateTimeField()
    
    def __str__(self):
        return '{} invited to {} by {}'.format(self.inviteeEmail, self.clique, self.inviter)

class Event(models.Model):
    clique = models.ForeignKey(Clique, on_delete=models.CASCADE, related_name='cliqueEvent', blank=True, null=True)#ONE TEAM CAN HAVE MANY EVENTS (ONE2M)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userEvent', blank=True, null=True)#ONE USER CAN HAVE MANY EVENTS (ONE2M)
    name = models.CharField(max_length=100, default='event')
    start = models.DateTimeField()
    end = models.DateTimeField()
    invited = models.ManyToManyField(User, related_name='eventInvited', blank=True, null=True)
    notGoing = models.ManyToManyField(User, related_name='notGoing', blank=True, null=True)
    details = models.CharField(max_length=100, default='This event is blah blah blah..')
    picture = models.CharField(max_length=100, default='pic1')
    def __str__(self):
        return f"{self.name} for {self.clique}."

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
    clique = models.ForeignKey(Clique, on_delete=models.CASCADE, related_name='cliqueAnnouncement')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventAnnouncement', blank=True, null=True)
    creator = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='creatorAnnouncement')
    priority = models.IntegerField(default=1)
    announcement = models.CharField(max_length=280, default='\"Do your hw\" -management')
    end = models.DateTimeField(blank=True, null=True)
    acknowledged = models.ManyToManyField(User, related_name='userAnnouncementAcknowledgment')
    def __str__(self):
        return f'{self.clique}: {self.announcement} with event {self.event}.'

class Reaction(models.Model):
    reactor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userReactor')
    reaction = models.CharField(max_length=100, choices=[("thumbs up", "THUMBS UP"),("dislike","DISLIKE")],  default=("dislike", "DISLIKE"))

class DirectMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userSenderDM')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userRecipientDM')
    message = models.CharField(max_length=500, default='message text')
    sentAt = models.DateTimeField()
    reaction = models.ManyToManyField(Reaction, related_name='directMessageReaction')

class CliqueMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userSenderCM')
    recipient = models.ForeignKey(Clique, on_delete=models.CASCADE, related_name='cliqueRecipientCM')
    message = models.CharField(max_length=500, default='message text')
    sentAt = models.DateTimeField()
    reaction = models.ManyToManyField(Reaction, related_name='cliqueMessageReaction')

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userToDo')
    name = models.CharField(max_length=100, default='laundry')
    due = models.DateTimeField()

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userRequest')
    clique = models.ForeignKey(Clique, on_delete=models.CASCADE, related_name='cliqueRequest')
    message = models.CharField(max_length=100, default='Please let me join our group.')
    dateRequested = models.DateTimeField()