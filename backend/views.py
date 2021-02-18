from django.http import HttpResponseRedirect, HttpResponse

def documentation(request):
    html = '''
    
    <html>
        <head>
            <title>OpusAPI</title>
        </head>
        <body>
            <p><a href="/admin/">/admin/</a> Django admin. Manage the database with a user friendly gui.</p>
            <a href="/tokenAuth/">/tokenAuth/</a> API View that receives a POST with a user's username and password. Returns a JSON Web Token that can be used for authenticated requests.

            <h1>Views</h1>
            <h3>User</h3>
            <ul>
                <li><a href="/currentUser/">/currentUser/</a></li>
                <li><a href="/users/">/users/</a></li>
                <li><a href="/users/register/">/users/register/</a></li>
                <li><a href="/users/admin/">/users/{username}/</a></li>
                <li><a href="/users/admin/teams/">/users/{username}/teams/</a></li>
                <li><a href="/users/admin/contacts/">/users/{username}/contacts/</a></li>
                <li><a href="/users/admin/schedule/">/users/{username}/schedule/</a></li>
            </ul>
            <h3>Team</h3>
            <ul>
                <li><a href="/teams/">/teams/</a></li>
                <li><a href="/teams/test/">/teams/{team}/</a></li>
                <li><a href="/teamDetails/Poodle People/">/teamDetails/{teamName}/</a></li>
                <li><a href="/teamMembers/Poodle People/">/teamMembers/{teamName}/</a></li>
            </ul>
            <h3>Invitation</h3>
            <ul>
                <li><a href="/invitations/">/invitations/</a></li>
                <li><a href="/invitations/1/">/invitation/{invitationId}/</a></li>
                <li><a href="/invitationDetails/abc123/">/invitationDetails/{inviteeEmail}/</a></li>
                <li><a href="/userInvitations/barackO/">/userInvitations/{username}/</a></li>
            </ul>
            <h3>Request</h3>
            <ul>
                <li><a href="/requests/">/requests/</a></li>
                <li><a href="/requests/1/">/requests/{requestId}/</a></li>
                <li><a href="/teamRequests/Dog Lovers/">/teamRequests/{teamName}/</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/events/">/events/</a></li>
                <li><a href="/events/1/">/events/{teamEventId}/</a></li>
                <li><a href="/teamEvents/Dog Lovers/">/teamEvents/{teamName}/</a></li>
            </ul>
            <h3>Schedule</h3>
            <ul>
                <li><a href="/schedules/">/schedules/</a></li>
                <li><a href="/schedules/1/">/schedules/{scheduleId}/</a></li>
                <li><a href="/userSchedules/barackO/">/userSchedules/{username}/</a></li>
                <li><a href="/timeFrames/">/timeframes/</a></li>
                <li><a href="/timeFrames/1/">/timeframes/{timeFrameId}/</a></li>
                <li><a href="/scheduleTimeFrames/1/">/scheduleTimeFrames/{scheduleId}/</a></li>
            </ul>
            <h3>Announcement</h3>
            <ul>
                <li><a href="/announcements/">/announcements/</a></li>
                <li><a href="/announcements/1/">/announcements/{announcementId}/</a></li>
                <li><a href="/teamAnnouncements/Dog Lovers/">/teamAnnouncements/{teamName}/</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)
