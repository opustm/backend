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
                <li><a href="/register/">/register/</a></li>
                <li><a href="/users/672e4b13-4b96-43f4-a420-c101ce2bee11/">/users/{userid}/</a></li>
                <li><a href="/users/672e4b13-4b96-43f4-a420-c101ce2bee11/teams/">/users/{userid}/teams/</a></li>
                <li><a href="/users/672e4b13-4b96-43f4-a420-c101ce2bee11/contacts/">/users/{userid}/contacts/</a></li>
                <li><a href="/users/672e4b13-4b96-43f4-a420-c101ce2bee11/schedule/">/users/{userid}/schedule/</a></li>
            </ul>
            <h3>Team</h3>
            <ul>
                <li><a href="/teams/">/teams/</a></li>
                <li><a href="/teams/1/">/teams/{teamid}/</a></li>
                <li><a href="/teams/1/members">/teams/{teamid}/members/</a></li>
            </ul>
            <h3>Request</h3>
            <ul>
                <li><a href="/requests/">/requests/</a></li>
                <li><a href="/requests/1/">/requests/{requestId}/</a></li>
                <li><a href="/requests/team/1/">/requests/team/{teamid}/</a></li>
                <li><a href="/requests/user/672e4b13-4b96-43f4-a420-c101ce2bee11/">/requests/user/{userid}/</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/events/">/events/</a></li>
                <li><a href="/events/1/">/events/{teamEventId}/</a></li>
                <li><a href="/events/team/1/">/events/team/{teamid}/</a></li>
                <li><a href="/events/user/672e4b13-4b96-43f4-a420-c101ce2bee11/">/events/user/{userid}/</a></li>
            </ul>
            <h3>Announcement</h3>
            <ul>
                <li><a href="/announcements/">/announcements/</a></li>
                <li><a href="/announcements/1/">/announcements/{announcementId}/</a></li>
                <li><a href="/announcements/team/1/">/announcements/team/{teamid}/</a></li>
                <li><a href="/announcements/user/672e4b13-4b96-43f4-a420-c101ce2bee11/">/announcements/user/{userid}/</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)
