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
                <li><a href="/users/test1/">/users/&lt;username&gt;/</a></li>
                <li><a href="/users/test1/teams/">/users/&lt;username&gt;/teams/</a></li>
                <li><a href="/users/test1/contacts/">/users/&lt;username&gt;/contacts/</a></li>
                <li><a href="/users/test1/schedule/">/users/&lt;username&gt;/schedule/</a></li>
                <li><a href="/userEmailDetails/barackO@example.com/">/userEmailDetails/&lt;userEmail&gt;/</a></li>
            </ul>
            <h3>Clique</h3>
            <ul>
                <li><a href="/cliques/">/cliques/</a></li>
                <li><a href="/cliques/1/">/cliques/&lt;cliqueId&gt;/</a></li>
                <li><a href="/cliqueDetails/Poodle People/">/cliqueDetails/&lt;cliqueName&gt;/</a></li>
                <li><a href="/cliqueMembers/Poodle People/">/cliqueMembers/&lt;cliqueName&gt;/</a></li>
            </ul>
            <h3>Invitation</h3>
            <ul>
                <li><a href="/invitations/">/invitations/</a></li>
                <li><a href="/invitations/1/">/invitation/&lt;invitationId&gt;/</a></li>
                <li><a href="/invitationDetails/abc123/">/invitationDetails/&lt;inviteeEmail&gt;/</a></li>
                <li><a href="/userInvitations/barackO/">/userInvitations/&lt;username&gt;/</a></li>
            </ul>
            <h3>Request</h3>
            <ul>
                <li><a href="/requests/">/requests/</a></li>
                <li><a href="/requests/1/">/requests/&lt;requestId&gt;/</a></li>
                <li><a href="/cliqueRequests/Dog Lovers/">/cliqueRequests/&lt;cliqueName&gt;/</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/events/">/events/</a></li>
                <li><a href="/events/1/">/events/&lt;cliqueEventId&gt;/</a></li>
                <li><a href="/cliqueEvents/Dog Lovers/">/cliqueEvents/&lt;cliqueName&gt;/</a></li>
            </ul>
            <h3>Schedule</h3>
            <ul>
                <li><a href="/schedules/">/schedules/</a></li>
                <li><a href="/schedules/1/">/schedules/&lt;scheduleId&gt;/</a></li>
                <li><a href="/userSchedules/barackO/">/userSchedules/&lt;username&gt;/</a></li>
                <li><a href="/timeFrames/">/timeframes/</a></li>
                <li><a href="/timeFrames/1/">/timeframes/&lt;timeFrameId&gt;/</a></li>
                <li><a href="/scheduleTimeFrames/1/">/scheduleTimeFrames/&lt;scheduleId&gt;/</a></li>
            </ul>
            <h3>Announcement</h3>
            <ul>
                <li><a href="/announcements/">/announcements/</a></li>
                <li><a href="/announcements/1/">/announcements/&lt;announcementId&gt;/</a></li>
                <li><a href="/cliqueAnnouncements/Dog Lovers/">/cliqueAnnouncements/&lt;cliqueName&gt;/</a></li>
            </ul>
            <h3>Message</h3>
            <ul>
                <li><a href="/directMessages/">/directMessages/</a></li>
                <li><a href="/directMessages/1/">/directMessages/&lt;directMessageId&gt;/</a></li>
                <li><a href="/userDirectMessagesSent/barackO/">/userDirectMessagesSent/&lt;userame&gt;/</a></li>
                <li><a href="/userDirectMessagesRecieved/barackO/">/userDirectMessagesRecieved/&lt;userame&gt;/</a></li>
                <li><a href="/cliqueMessages/">/cliqueMessages/</a></li>
                <li><a href="/cliqueMessages/1/">/cliqueMessages/&lt;cliqueMessageId&gt;/</a></li>
                <li><a href="/cliqueCliqueMessages/Dog Lovers/">/cliqueCliqueMessages/&lt;cliqueName&gt;/</a></li>
                <li><a href="/reactions/">/reactions/</a></li>
                <li><a href="/reactions/1/">/reactions/&lt;reactionId&gt;/</a></li>
            </ul>
            <h3>To Do</h3>
            <ul>
                <li><a href="/toDos/">/toDos/</a></li>
                <li><a href="/toDos/1/">/toDos/&lt;toDoId&gt;/</a></li>
                <li><a href="/userToDos/barackO/">/userToDos/&lt;username&gt;/</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)
