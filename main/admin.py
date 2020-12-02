from django.contrib import admin
from main.models import User, Team, Event, Invitation, WeeklyAvailability


admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(WeeklyAvailability)
admin.site.register(Invitation)