
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.http import Http404
from uuid import UUID

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
import json

from .models import Event, ToDo, Request, Invitation, User, Clique, Schedule, TimeFrame, Announcement, Reaction, DirectMessage, CliqueMessage
from .serializers import CliqueSerializer, RequestSerializer, ToDoSerializer, UserSerializer, AnnouncementSerializer, InvitationSerializer, EventSerializer, UserSerializerWithToken, ScheduleSerializer, TimeFrameSerializer, ReactionSerializer, DirectMessageSerializer, CliqueMessageSerializer

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
        serializer = UserSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        inv = self.get_object(username)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserEmailDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, userEmail):
        try:
            return User.objects.get(email=userEmail)
        except User.DoesNotExist:
            return False

    def get(self, request, userEmail, format=None):
        user = self.get_object(userEmail)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, userEmail, format=None):
        inv = self.get_object(userEmail)
        serializer = UserSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userEmail, format=None):
        inv = self.get_object(userEmail)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserTeams(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object_byid(self, id):
        try:
            return Clique.objects.get(id=id)
        except Clique.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('username', 'id')
        teamQuerySet = Clique.objects.values('members', 'managers', 'owners', 'id')
        print(teamQuerySet)
        teams = []
        userId = ''
        for user in userQuerySet:
            if user['username'] == username:
                userId = user['id']

        if userId:
            for team in teamQuerySet:
                members = team['members']
                managers = team['managers']
                owners = team['owners']
                if userId == members or userId == managers or userId == owners:
                    teamObject = self.get_object_byid(team['id'])
                    serializedTeam = CliqueSerializer(teamObject).data
                    if not serializedTeam in teams:
                        teams.append(serializedTeam)
                
            return Response(teams, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)

class CliqueDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, name):
        try:
            return Clique.objects.get(name=name)
        except Clique.DoesNotExist:
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
        cliqueQuerySet = Clique.objects.values('id', 'name')
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

class CliqueIdMembers(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return False
    def get(self, request, id, format=None):
        userQuerySet=User.objects.values('id', 'cliques')
        members=[]
        for user in userQuerySet:
            if user["cliques"]==id:
                members.append(UserSerializer(self.get_object(user['id'])).data)
        if members:
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class RelatedCliques(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object_byid(self, id):
        try:
            return Clique.objects.get(id=id)
        except Clique.DoesNotExist:
            return False
    def get(self, request, name, format=None):
        cliqueQuerySet = Clique.objects.values('relatedCliques', 'name')
        related=[]
        for clique in cliqueQuerySet:
            if clique['name']==name:
                related.append(clique['relatedCliques'])
        if related:
            members=[]
            for cliqueid in related:
                members.append(CliqueSerializer(self.get_object_byid(cliqueid)).data)
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ManyRelatedCliques(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object_byid(self, id):
        try:
            return Clique.objects.get(id=id)
        except Clique.DoesNotExist:
            return False
    def get(self, request, names, format=None):
        nameList=names.split('&')
        allCliquesRelatedCliques={}
        for name in nameList:
            cliqueQuerySet = Clique.objects.values('relatedCliques', 'name')
            related=[]
            for clique in cliqueQuerySet:
                if clique['name']==name:
                    related.append(clique['relatedCliques'])
            if related:
                members=[]
                for cliqueid in related:
                    members.append(CliqueSerializer(self.get_object_byid(cliqueid)).data)
                allCliquesRelatedCliques[name]=members
            else:
                allCliquesRelatedCliques[name]="404_NOT_FOUND"
        if allCliquesRelatedCliques:
            return Response(allCliquesRelatedCliques, status=status.HTTP_200_OK)
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
        cliqueQuerySet = Clique.objects.values('id', 'name')
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

class UserEvents(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, eventid):
        try:
            return Event.objects.get(id=eventid)
        except Event.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            eventQuerySet=Event.objects.values('id', 'user')
            events=[]
            for event in eventQuerySet:
                if event["user"]==userid:
                    events.append(EventSerializer(self.get_object(event['id'])).data)
            return Response(events, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserInvitations(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, invitationId):
        try:
            return Invitation.objects.get(id=invitationId)
        except Invitation.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            invitationQuerySet=Invitation.objects.values('id', 'invitee')
            invitations=[]
            for invitation in invitationQuerySet:
                if invitation["invitee"]==userid:
                    invitations.append(InvitationSerializer(self.get_object(invitation['id'])).data)
            return Response(invitations, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CliqueRequests(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, requestId):
        try:
            return Request.objects.get(id=requestId)
        except Request.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        cliqueQuerySet = Clique.objects.values('id', 'name')
        cliqueid=None
        for clique in cliqueQuerySet:
            if clique['name']==name:
                cliqueid=clique['id']
        if cliqueid:
            requestQuerySet=Request.objects.values('id', 'clique')
            requests=[]
            for request in requestQuerySet:
                if request["clique"]==cliqueid:
                    requests.append(RequestSerializer(self.get_object(request['id'])).data)
            return Response(requests, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class InvitationDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, inviteeEmail):
        try:
            return Invitation.objects.get(inviteeEmail=inviteeEmail)
        except Invitation.DoesNotExist:
            return False

    def get(self, request, inviteeEmail, format=None):
        inv = self.get_object(inviteeEmail)
        if inv:
            serializer = InvitationSerializer(inv)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, inviteeEmail, format=None):
        inv = self.get_object(inviteeEmail)
        serializer = InvitationSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, inviteeEmail, format=None):
        inv = self.get_object(inviteeEmail)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




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
        cliqueQuerySet = Clique.objects.values('id', 'name')
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

class CliqueCliqueMessages(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, cliquemessageid):
        try:
            return CliqueMessage.objects.get(id=cliquemessageid)
        except CliqueMessage.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        cliqueQuerySet = Clique.objects.values('id', 'name')
        cliqueid=None
        for clique in cliqueQuerySet:
            if clique['name']==name:
                cliqueid=clique['id']
        if cliqueid:
            cliqueMessageQuerySet=CliqueMessage.objects.values('id', 'clique')
            cliqueMessages=[]
            for cliqueMessage in cliqueMessageQuerySet:
                if cliqueMessage["clique"]==cliqueid:
                    cliqueMessages.append(CliqueMessageSerializer(self.get_object(cliqueMessage['id'])).data)
            return Response(cliqueMessages, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserDirectMessagesSent(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, directMessageid):
        try:
            return DirectMessage.objects.get(id=directMessageid)
        except DirectMessage.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            directMessageQuerySet = DirectMessage.objects.values('sender', 'id')
            idsOfUsersDirectMessages=[]
            for directMessage in directMessageQuerySet:
                if directMessage['sender']==userid:
                    idsOfUsersDirectMessages.append(directMessage['id'])
            if idsOfUsersDirectMessages:
                directMessages=[]
                for directMessageid in idsOfUsersDirectMessages:
                    directMessages.append(DirectMessageSerializer(self.get_object(directMessageid)).data)
                if directMessages:
                    return Response(directMessages, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserDirectMessagesRecieved(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, directMessageid):
        try:
            return DirectMessage.objects.get(id=directMessageid)
        except DirectMessage.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            directMessageQuerySet = DirectMessage.objects.values('recipient', 'id')
            idsOfUsersDirectMessages=[]
            for directMessage in directMessageQuerySet:
                if directMessage['recipient']==userid:
                    idsOfUsersDirectMessages.append(directMessage['id'])
            if idsOfUsersDirectMessages:
                directMessages=[]
                for directMessageid in idsOfUsersDirectMessages:
                    directMessages.append(DirectMessageSerializer(self.get_object(directMessageid)).data)
                if directMessages:
                    return Response(directMessages, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserToDos(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, toDoid):
        try:
            return ToDo.objects.get(id=toDoid)
        except ToDo.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            toDoQuerySet = ToDo.objects.values('user', 'id')
            idsOfUsersToDos=[]
            for toDo in toDoQuerySet:
                if toDo['user']==userid:
                    idsOfUsersToDos.append(toDo['id'])
            if idsOfUsersToDos:
                toDos=[]
                for toDoid in idsOfUsersToDos:
                    toDos.append(ToDoSerializer(self.get_object(toDoid)).data)
                if toDos:
                    return Response(toDos, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


def index(request):
    permission_classes = (permissions.AllowAny,)
    return HttpResponse("Welcome to the OPUS-TM API")

@api_view(['GET'])
def current_user(request):
    permission_classes = (permissions.AllowAny,)
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)