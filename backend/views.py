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
                <li><a href="/users/admin/">/users/{username}/</a></li>
                <li><a href="/users/admin/teams/">/users/{username}/teams/</a></li>
                <li><a href="/users/admin/contacts/">/users/{username}/contacts/</a></li>
                <li><a href="/users/admin/schedule/">/users/{username}/schedule/</a></li>
            </ul>
            <h3>Team</h3>
            <ul>
                <li><a href="/teams/">/teams/</a></li>
                <li><a href="/teams/test/">/teams/{teamName}/</a></li>
                <li><a href="/teams/test/members">/teams/{teamName}/members/</a></li>
            </ul>
            <h3>Invitation</h3>
            <h3>Request</h3>
            <ul>
                <li><a href="/requests/">/requests/</a></li>
                <li><a href="/requests/1/">/requests/{requestId}/</a></li>
                <li><a href="/requests/team/test/">/requests/team/{teamName}/</a></li>
                <li><a href="/requests/user/admin/">/requests/user/{username}/</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/events/">/events/</a></li>
                <li><a href="/events/1/">/events/{teamEventId}/</a></li>
                <li><a href="/events/team/test/">/events/team/{teamName}/</a></li>
                <li><a href="/events/user/admin/">/events/user/{username}/</a></li>
            </ul>
            <h3>Announcement</h3>
            <ul>
                <li><a href="/announcements/">/announcements/</a></li>
                <li><a href="/announcements/1/">/announcements/{announcementId}/</a></li>
                <li><a href="/announcements/team/test/">/announcements/team/{teamName}/</a></li>
                <li><a href="/announcements/user/admin/">/announcements/user/{username}/</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)
