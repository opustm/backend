
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.http import Http404

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
import json

from .models import *
from .serializers import *

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
            return Team.objects.get(id=id)
        except Team.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('username', 'id')
        teamQuerySet = Team.objects.values('members', 'managers', 'owners', 'id')
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
                    serializedTeam = TeamSerializer(teamObject).data
                    if not serializedTeam in teams:
                        teams.append(serializedTeam)
                
            return Response(teams, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)

class UserContacts(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object_byid(self, id):
        try:
            return Team.objects.get(id=id)
        except Team.DoesNotExist:
            return False

    def get_user_object_byid(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('username', 'id')
        teamQuerySet = Team.objects.values('members', 'managers', 'owners', 'id')
        seen = set()
        teams = set()
        contacts = []
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
                    teams.add(team['id'])

            newTeamQuerySet = Team.objects.values('members', 'managers', 'owners', 'id')
            
            for team in newTeamQuerySet:
                if team['id'] in teams:
                    members = team['members']
                    managers = team['managers']
                    owners = team['owners']
                    for user in [members, managers, owners]:
                        if user != userId:
                            contact = self.get_user_object_byid(user)
                            if contact:
                                if not user in seen:
                                    serializedContact = UserSerializer(contact).data
                                    contacts.append(serializedContact)
                                    seen.add(user)
                
            return Response(list(contacts), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserSchedule(APIView):
    def getScheduleObject(self, id):
        try:
            return Schedule.objects.get(user = id)
        except User.DoesNotExist:
            return False

    def get(self, request, username):
        userQuerySet = User.objects.values('username', 'id')
        scheduleQuerySet = Schedule.objects.values('user')

        userId = ''
        for user in userQuerySet:
            if user['username'] == username:
                userId = user['id']
        if userId:
            for schedule in scheduleQuerySet:
                if schedule['user'] == userId:
                    scheduleObject = self.getScheduleObject(userId)
                    serializedSchedule = ScheduleSerializer(scheduleObject).data
                    return Response(serializedSchedule, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class TeamDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, name):
        try:
            return Team.objects.get(name=name)
        except Team.DoesNotExist:
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

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('name', 'members', 'managers', 'owners')
        members={}
        for team in teamQuerySet:
            if team['name']==name:
                for level in ['members', 'managers', 'owners']:
                    print(team[level])
                    if not team[level] is None:
                        print(team[level])
                        users=[]
                        if isinstance(team[level], list):
                            for user in team[level]:
                                users.append(UserSerializer(self.get_object(user)).data)
                        else:
                            users.append(UserSerializer(self.get_object(team[level])).data)
                        members[level]=users
                    else:
                        members[level]=[]

        if members:
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TeamIdMembers(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return False
    def get(self, request, id, format=None):
        userQuerySet=User.objects.values('id', 'teams')
        members=[]
        for user in userQuerySet:
            if user["teams"]==id:
                members.append(UserSerializer(self.get_object(user['id'])).data)
        if members:
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class RelatedTeams(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object_byid(self, id):
        try:
            return Team.objects.get(id=id)
        except Team.DoesNotExist:
            return False
    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('relatedTeams', 'name')
        related=[]
        for team in teamQuerySet:
            if team['name']==name:
                related.append(team['relatedTeams'])
        if related:
            members=[]
            for teamid in related:
                members.append(TeamSerializer(self.get_object_byid(teamid)).data)
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ManyRelatedTeams(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object_byid(self, id):
        try:
            return Team.objects.get(id=id)
        except Team.DoesNotExist:
            return False
    def get(self, request, names, format=None):
        nameList=names.split('&')
        allTeamsRelatedTeams={}
        for name in nameList:
            teamQuerySet = Team.objects.values('relatedTeams', 'name')
            related=[]
            for team in teamQuerySet:
                if team['name']==name:
                    related.append(team['relatedTeams'])
            if related:
                members=[]
                for teamid in related:
                    members.append(TeamSerializer(self.get_object_byid(teamid)).data)
                allTeamsRelatedTeams[name]=members
            else:
                allTeamsRelatedTeams[name]="404_NOT_FOUND"
        if allTeamsRelatedTeams:
            return Response(allTeamsRelatedTeams, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TeamEvents(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, eventid):
        try:
            return Event.objects.get(id=eventid)
        except Event.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('id', 'name')
        teamid=None
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            eventQuerySet=Event.objects.values('id', 'team')
            events=[]
            for event in eventQuerySet:
                if event["team"]==teamid:
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

class TeamRequests(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, requestId):
        try:
            return Request.objects.get(id=requestId)
        except Request.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('id', 'name')
        teamid=None
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            requestQuerySet=Request.objects.values('id', 'team')
            requests=[]
            for request in requestQuerySet:
                if request["team"]==teamid:
                    requests.append(RequestSerializer(self.get_object(request['id'])).data)
            return Response(requests, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserRequests(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, requestId):
        try:
            return Request.objects.get(id=requestId)
        except Request.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['name']==username:
                userid=user['id']
        if userid:
            requestQuerySet=Request.objects.values('id', 'user')
            requests=[]
            for request in requestQuerySet:
                if request["user"]==userid:
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

class TeamAnnouncements(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, announcementid):
        try:
            return Announcement.objects.get(id=announcementid)
        except Announcement.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('id', 'name')
        teamid=None
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            announcementQuerySet=Announcement.objects.values('id', 'team')
            announcements=[]
            for announcement in announcementQuerySet:
                if announcement["team"]==teamid:
                    announcements.append(AnnouncementSerializer(self.get_object(announcement['id'])).data)
            return Response(announcements, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserAnnouncements(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, announcementid):
        try:
            return Announcement.objects.get(id=announcementid)
        except Announcement.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            announcementQuerySet=Announcement.objects.values('id', 'creator')
            announcements=[]
            for announcement in announcementQuerySet:
                if announcement["creator"]==userid:
                    announcements.append(AnnouncementSerializer(self.get_object(announcement['id'])).data)
            return Response(announcements, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

# class TeamTeamMessages(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def get_object(self, teammessageid):
#         try:
#             return TeamMessage.objects.get(id=teammessageid)
#         except TeamMessage.DoesNotExist:
#             return False

#     def get(self, request, name, format=None):
#         teamQuerySet = Team.objects.values('id', 'name')
#         teamid=None
#         for team in teamQuerySet:
#             if team['name']==name:
#                 teamid=team['id']
#         if teamid:
#             teamMessageQuerySet=TeamMessage.objects.values('id', 'team')
#             teamMessages=[]
#             for teamMessage in teamMessageQuerySet:
#                 if teamMessage["team"]==teamid:
#                     teamMessages.append(TeamMessageSerializer(self.get_object(teamMessage['id'])).data)
#             return Response(teamMessages, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# class UserDirectMessagesSent(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def get_object(self, directMessageid):
#         try:
#             return DirectMessage.objects.get(id=directMessageid)
#         except DirectMessage.DoesNotExist:
#             return False

#     def get(self, request, username, format=None):
#         userQuerySet = User.objects.values('id', 'username')
#         userid=None
#         for user in userQuerySet:
#             if user['username']==username:
#                 userid=user['id']
#         if userid:
#             directMessageQuerySet = DirectMessage.objects.values('sender', 'id')
#             idsOfUsersDirectMessages=[]
#             for directMessage in directMessageQuerySet:
#                 if directMessage['sender']==userid:
#                     idsOfUsersDirectMessages.append(directMessage['id'])
#             if idsOfUsersDirectMessages:
#                 directMessages=[]
#                 for directMessageid in idsOfUsersDirectMessages:
#                     directMessages.append(DirectMessageSerializer(self.get_object(directMessageid)).data)
#                 if directMessages:
#                     return Response(directMessages, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)

# class UserDirectMessagesRecieved(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def get_object(self, directMessageid):
#         try:
#             return DirectMessage.objects.get(id=directMessageid)
#         except DirectMessage.DoesNotExist:
#             return False

#     def get(self, request, username, format=None):
#         userQuerySet = User.objects.values('id', 'username')
#         userid=None
#         for user in userQuerySet:
#             if user['username']==username:
#                 userid=user['id']
#         if userid:
#             directMessageQuerySet = DirectMessage.objects.values('recipient', 'id')
#             idsOfUsersDirectMessages=[]
#             for directMessage in directMessageQuerySet:
#                 if directMessage['recipient']==userid:
#                     idsOfUsersDirectMessages.append(directMessage['id'])
#             if idsOfUsersDirectMessages:
#                 directMessages=[]
#                 for directMessageid in idsOfUsersDirectMessages:
#                     directMessages.append(DirectMessageSerializer(self.get_object(directMessageid)).data)
#                 if directMessages:
#                     return Response(directMessages, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)



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
