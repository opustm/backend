from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions, status


class TeamViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class InvitationViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Invitation.objects.all()
    serializer_class = serializers.InvitationSerializer


class EventViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class ScheduleViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer


class TimeFrameViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.TimeFrame.objects.all()
    serializer_class = serializers.TimeFrameSerializer


class AnnouncementViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer


# class DirectMessageViewset(viewsets.ModelViewSet):
#     permission_classes = (permissions.AllowAny,)
#     queryset= models.DirectMessage.objects.all()
#     serializer_class = serializers.DirectMessageSerializer

# class TeamMessageViewset(viewsets.ModelViewSet):
#     permission_classes = (permissions.AllowAny,)
#     queryset= models.TeamMessage.objects.all()
#     serializer_class = serializers.TeamMessageSerializer

# class ReactionViewset(viewsets.ModelViewSet):
#     permission_classes = (permissions.AllowAny,)
#     queryset= models.Reaction.objects.all()
#     serializer_class = serializers.ReactionSerializer


class RequestViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer
