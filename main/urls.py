from django.urls import path, include
from .views import current_user, UserList, CliqueRequests, UserEmailDetails, CliqueIdMembers, InvitationDetails, UserToDos, index, UserDetails, CliqueDetails, CliqueEvents, UserInvitations, CliqueMembers, UserSchedules, ScheduleTimeFrames, CliqueAnnouncements, CliqueCliqueMessages, UserDirectMessagesSent, UserDirectMessagesRecieved, UserCliques, RelatedCliques, ManyRelatedCliques

urlpatterns = [
    path('', index),
    path('currentUser/', current_user),
    path('addUsers/', UserList.as_view()),
    path('userDetails/<str:username>/', UserDetails.as_view()),
    path('userEmailDetails/<str:userEmail>/', UserEmailDetails.as_view()),
    path('cliqueDetails/<str:name>/', CliqueDetails.as_view()),
    path('cliqueMembers/<str:name>/', CliqueMembers.as_view()),    
    path('cliqueidMembers/<int:id>/', CliqueIdMembers.as_view()),    
    path('cliqueAnnouncements/<str:name>/', CliqueAnnouncements.as_view()),  
    path('userInvitations/<str:username>/', UserInvitations.as_view()),
    path('invitationDetails/<str:inviteeEmail>/', InvitationDetails.as_view()),
    path('cliqueRequests/<str:cliqueName>/', CliqueRequests.as_view()),
    path('cliqueEvents/<str:name>/', CliqueEvents.as_view()),
    path('userSchedules/<str:username>/', UserSchedules.as_view()),
    path('scheduleTimeFrames/<int:scheduleId>/', ScheduleTimeFrames.as_view()),
    path('cliqueCliqueMesssages/<str:name>/', CliqueCliqueMessages.as_view()),
    path('userDirectMessagesSent/<str:username>/', UserDirectMessagesSent.as_view()),
    path('userDirectMessagesRecieved/<str:username>/', UserDirectMessagesRecieved.as_view()),
    path('userToDos/<str:username>/', UserToDos.as_view()),
    path('relatedCliques/<str:name>/', RelatedCliques.as_view()),
    path('manyRelatedCliques/<str:names>/', ManyRelatedCliques.as_view()),
    path('userCliques/<str:username>/', UserCliques.as_view()),
]
