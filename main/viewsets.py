from rest_framework import viewsets
from . import models
from . import serializers

class TeamViewset(viewsets.ModelViewSet):
    queryset= models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    
class UserViewset(viewsets.ModelViewSet):
    queryset= models.User.objects.all()
    serializer_class = serializers.UserSerializerTest

class InvitationViewset(viewsets.ModelViewSet):
    queryset= models.Invitation.objects.all()
    serializer_class = serializers.InvitationSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset= models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class WeeklyAvailabilityViewset(viewsets.ModelViewSet):
    queryset= models.WeeklyAvailability.objects.all()
    serializer_class = serializers.WeeklyAvailabilitySerializer