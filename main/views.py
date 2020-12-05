
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.http import Http404

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Event, Invitation, User, SoloEvent, OpusTeam, OpusClique, Schedule, TimeFrame, Announcement
from .serializers import TeamSerializer, CliqueSerializer, UserSerializer, AnnouncementSerializer, InvitationSerializer, EventSerializer, SoloEventSerializer, UserSerializerWithToken, ScheduleSerializer, TimeFrameSerializer

class UserDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        user = self.get_object(username)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, username, format=None):
        inv = self.get_object(username)
        serializer = InvitationSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        inv = self.get_object(username)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, name):
        try:
            return OpusTeam.objects.get(name=name)
        except OpusTeam.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        team = self.get_object(name)
        if team:
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, name, format=None):
        team = self.get_object(name)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        team = self.get_object(name)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamMembers(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return False
    def get(self, request, name, format=None):
        teamQuerySet = OpusTeam.objects.values('id', 'name')
        teamid=None
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            userQuerySet=User.objects.values('username', 'teams')
            members=[]
            for user in userQuerySet:
                if user["teams"]==teamid:
                    members.append(UserSerializer(self.get_object(user['username'])).data)
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CliqueDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, name):
        try:
            return OpusClique.objects.get(name=name)
        except OpusClique.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        clique = self.get_object(name)
        if clique:
            serializer = CliqueSerializer(clique)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, name, format=None):
        clique = self.get_object(name)
        serializer = CliqueSerializer(clique, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        clique = self.get_object(name)
        clique.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CliqueMembers(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return False
    def get(self, request, name, format=None):
        cliqueQuerySet = OpusClique.objects.values('id', 'name')
        cliqueid=None
        for clique in cliqueQuerySet:
            if clique['name']==name:
                cliqueid=clique['id']
        if cliqueid:
            userQuerySet=User.objects.values('username', 'cliques')
            members=[]
            for user in userQuerySet:
                if user["cliques"]==cliqueid:
                    members.append(UserSerializer(self.get_object(user['username'])).data)
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CliqueEvents(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, eventid):
        try:
            return Event.objects.get(id=eventid)
        except Event.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        cliqueQuerySet = OpusClique.objects.values('id', 'name')
        cliqueid=None
        for clique in cliqueQuerySet:
            if clique['name']==name:
                cliqueid=clique['id']
        if cliqueid:
            eventQuerySet=Event.objects.values('id', 'clique')
            events=[]
            for event in eventQuerySet:
                if event["clique"]==cliqueid:
                    events.append(EventSerializer(self.get_object(event['id'])).data)
            return Response(events, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class InvitationDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, code):
        try:
            return Invitation.objects.get(code=code)
        except Invitation.DoesNotExist:
            return False

    def get(self, request, code, format=None):#has to be by code unless it is a registered user.
        inv = self.get_object(code)
        if inv:
            serializer = InvitationSerializer(inv)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, code, format=None):
        inv = self.get_object(code)
        serializer = InvitationSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        inv = self.get_object(code)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserSoloEvents(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, eventid):
        try:
            return SoloEvent.objects.get(id=eventid)
        except SoloEvent.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            eventQuerySet=SoloEvent.objects.values('id', 'user')
            events=[]
            for event in eventQuerySet:
                if event["user"]==userid:
                    events.append(SoloEventSerializer(self.get_object(event['id'])).data)
            return Response(events, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserSchedules(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, scheduleid):
        try:
            return Schedule.objects.get(id=scheduleid)
        except Schedule.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            scheduleQuerySet = Schedule.objects.values('user', 'id')
            idsOfUsersSchedules=[]
            for schedule in scheduleQuerySet:
                if schedule['user']==userid:
                    idsOfUsersSchedules.append(schedule['id'])
            if idsOfUsersSchedules:
                schedules=[]
                for scheduleid in idsOfUsersSchedules:
                    schedules.append(ScheduleSerializer(self.get_object(scheduleid)).data)
                if schedules:
                    return Response(schedules, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ScheduleTimeFrames(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, timeframeid):
        try:
            return TimeFrame.objects.get(id=timeframeid)
        except TimeFrame.DoesNotExist:
            return False

    def get(self, request, scheduleId, format=None):
        timeFrameQuerySet = TimeFrame.objects.values('id', 'schedule')
        timeframeids=[]
        for timeFrame in timeFrameQuerySet:
            if timeFrame['schedule']==scheduleId:
                timeframeids.append(timeFrame['id'])
        if timeframeids:
            timeframes=[]
            for timeframeid in timeframeids:
                timeframes.append(TimeFrameSerializer(self.get_object(timeframeid)).data)
            if timeframes:
                return Response(timeframes, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CliqueAnnouncements(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, announcementid):
        try:
            return Announcement.objects.get(id=announcementid)
        except Announcement.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        cliqueQuerySet = OpusClique.objects.values('id', 'name')
        cliqueid=None
        for clique in cliqueQuerySet:
            if clique['name']==name:
                cliqueid=clique['id']
        if cliqueid:
            announcementQuerySet=Announcement.objects.values('id', 'clique')
            announcements=[]
            for announcement in announcementQuerySet:
                if announcement["clique"]==cliqueid:
                    announcements.append(AnnouncementSerializer(self.get_object(announcement['id'])).data)
            return Response(announcements, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


def index(request):
    return HttpResponse("Welcome to the OPUS-TM API")

@api_view(['GET'])
def team(request):
    serializer=TeamSerializer(request.team)
    return Response(serializer.data)

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
