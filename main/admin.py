from django.contrib import admin
from main.models import User, Team, Event, Invitation, TimeFrame, Schedule, Announcement, Reaction, DirectMessage, TeamMessage, ToDo, Request


admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Schedule)
admin.site.register(TimeFrame)
admin.site.register(Invitation)
admin.site.register(Announcement)
admin.site.register(Reaction)
admin.site.register(DirectMessage)
admin.site.register(TeamMessage)
admin.site.register(ToDo)
admin.site.register(Request)