from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index),
    path("currentUser/", current_user),
    path("register/", UserList.as_view()),
    path("users/<str:userid>/teams/", UserTeams.as_view(), name="get_teams_by_userid"),
    path(
        "users/<str:userid>/contacts/",
        UserContacts.as_view(),
        name="get_contacts_by_userid",
    ),
    path(
        "users/<str:userid>/schedule/",
        UserSchedule.as_view(),
        name="get_schedule_by_userid",
    ),
    path(
        "teams/<str:teamid>/members/",
        TeamMembers.as_view(),
        name="get_members_by_userid",
    ),
    path(
        "announcements/team/<str:teamid>/",
        TeamAnnouncements.as_view(),
        name="get_team_announcements_by_teamid",
    ),
    path(
        "announcements/user/<str:userid>/",
        UserAnnouncements.as_view(),
        name="get_user_announcements_by_userid",
    ),
    path(
        "events/team/<str:teamid>/",
        TeamEvents.as_view(),
        name="get_team_events_by_teamid",
    ),
    path(
        "events/user/<str:userid>/",
        UserEvents.as_view(),
        name="get_user_events_by_userid",
    ),
    path(
        "requests/team/<str:teamid>/",
        TeamRequests.as_view(),
        name="get_team_requests_by_teamid",
    ),
    path(
        "requests/user/<str:userid>/",
        UserRequests.as_view(),
        name="get_user_requests_by_userid",
    ),
    # path('userInvitations/<str:username>/', UserInvitations.as_view()),
    # path('teamInvitations/<str:name>/', InvitationDetails.as_view()),
    # path('userSchedules/<str:username>/', UserSchedules.as_view()),
    # path('scheduleTimeFrames/<int:scheduleId>/', ScheduleTimeFrames.as_view()),
    # path('relatedTeams/<str:name>/', RelatedTeams.as_view()),
    # path('manyRelatedTeams/<str:names>/', ManyRelatedTeams.as_view())
]
