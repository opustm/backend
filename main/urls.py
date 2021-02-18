from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('currentUser/', current_user),
    path('register/', UserList.as_view()),
    path('users/<str:username>/', UserDetails.as_view()),
    path('users/<str:username>/teams/',UserTeams.as_view()),
    path('users/<str:username>/contacts/',UserContacts.as_view()),
    path('users/<str:username>/schedule/',UserSchedule.as_view()),

    path('teams/<str:name>/', TeamDetails.as_view()),
    path('teams/<str:name>/members/', TeamMembers.as_view()),
  
    path('announcements/team/<str:name>/', TeamAnnouncements.as_view()),  
    path('announcements/user/<str:username>/', UserAnnouncements.as_view()),  

    path('events/team/<str:name>/', TeamEvents.as_view()),
    path('events/user/<str:username>/', UserEvents.as_view()),

    path('requests/team/<str:name>/', TeamRequests.as_view()),
    path('requests/user/<str:userame>/', UserRequests.as_view()),

    # path('userInvitations/<str:username>/', UserInvitations.as_view()),
    # path('teamInvitations/<str:name>/', InvitationDetails.as_view()),

    # path('userSchedules/<str:username>/', UserSchedules.as_view()),
    # path('scheduleTimeFrames/<int:scheduleId>/', ScheduleTimeFrames.as_view()),

    # path('relatedTeams/<str:name>/', RelatedTeams.as_view()),
    # path('manyRelatedTeams/<str:names>/', ManyRelatedTeams.as_view())
]
