from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('currentUser/', current_user),
    path('register/', UserList.as_view()),
    
    path('users/<str:userid>/teams/',UserTeams.as_view()),
    path('users/<str:userid>/contacts/',UserContacts.as_view()),
    path('users/<str:userid>/schedule/',UserSchedule.as_view()),

    path('teams/<str:teamid>/members/', TeamMembers.as_view()),
  
    path('announcements/team/<str:teamid>/', TeamAnnouncements.as_view()),  
    path('announcements/user/<str:userid>/', UserAnnouncements.as_view()),  

    path('events/team/<str:teamid>/', TeamEvents.as_view()),
    path('events/user/<str:userid>/', UserEvents.as_view()),

    path('requests/team/<str:teamid>/', TeamRequests.as_view()),
    path('requests/user/<str:userame>/', UserRequests.as_view()),

    # path('userInvitations/<str:username>/', UserInvitations.as_view()),
    # path('teamInvitations/<str:name>/', InvitationDetails.as_view()),

    # path('userSchedules/<str:username>/', UserSchedules.as_view()),
    # path('scheduleTimeFrames/<int:scheduleId>/', ScheduleTimeFrames.as_view()),

    # path('relatedTeams/<str:name>/', RelatedTeams.as_view()),
    # path('manyRelatedTeams/<str:names>/', ManyRelatedTeams.as_view())
]
