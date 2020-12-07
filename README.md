## Home to the opus-tm Django REST [API](https://opustm-api.herokuapp.com/)
## This API serves our React Web [App](https://opustm.herokuapp.com/)

### Test Users: (password and username are the same, email is &lt;username&gt;@example.com)
- test
- dvader
- lukeskywalker
- leiaskywalker

### Test Cliques:
- Test
- The Dark Side

# Endpoints:
## User
- /currentUser/
- /addUsers/                  
- /users/                         
- /users/&lt;userId&gt;/
- /userDetails/&lt;username&gt;/
- /userEmailDetails/&lt;userEmail&gt;/
## Clique
- /cliques/
- /cliques/&lt;cliqueId&gt;/
- /cliqueDetails/&lt;cliqueName&gt;/
- /cliqueMembers/&lt;cliqueName&gt;/
## Invitation
- /invitations/
- /invitation/&lt;invitationId&gt;/
- /invitationDetails/&lt;inviteeEmail&gt;/
- /userInvitations/&lt;username&gt;/
## Request
- /requests/
- /requests/&lt;requestId&gt;/
- /cliqueRequests/&lt;cliqueName&gt;/
## Event
- /events/
- /events/&lt;cliqueEventId&gt;/
- /cliqueEvents/&lt;cliqueName&gt;/
- /soloEvents/
- /soloEvents/&lt;userEventId&gt;/
- /userSoloEvents/&lt;username&gt;/
## Schedule
- /schedules/
- /schedules/&lt;scheduleId&gt;/
- /userSchedules/&lt;username&gt;/
- /timeframes/
- /timeframes/&lt;timeFrameId&gt;/
- /scheduleTimeFrames/&lt;scheduleId&gt;/
## Announcement
- /announcements/
- /announcements/&lt;announcementId&gt;/
- /cliqueAnnouncements/&lt;cliqueName&gt;/
## Message
- /directMessages/
- /directMessages/&lt;directMessageId&gt;/
- /userDirectMessagesSent/&lt;username&gt;/
- /userDirectMessagesRecieved/&lt;username&gt;/
- /cliqueMessages/
- /cliqueMessages/&lt;cliqueMessageId&gt;/
- /cliqueCliqueMessages/&lt;cliqueName&gt;/
- /reactions/
- /reactions/&lt;reactionId&gt;/
## To Do
- /toDos/
- /toDos/&lt;toDoId&gt;/
- /userToDos/&lt;username&gt;/
## Token
- /tokenAuth/
## Django Admin
- /admin/

## DEPLOYMENT: 
For now we have stuck to Heroku for the sake of familiarity. Future plans possibly include deplyment on AWS. To ensure that we always have a working build, we also deploy a staging build to use in development:
[Staging Build](https://opustm-api-staging.herokuapp.com/)

## DATABASE: 
PostgreSQL. We mainly decided on this because of the ease of access with Heroku. However, we are also able to configure Django to run SQLite when testing locally. The pros and cons of each are described well in this [article](https://tableplus.com/blog/2018/08/sqlite-vs-postgresql-which-database-to-use-and-why.html)

## DJANGO MODEL & DIAGRAM: 
Django enables the creation of database model objects in python. Once each model is created, Django automatically creates migrations in which it can create, update, and generate SQL to add to the database based on the python models. The structure of the database is depicted in model.py:

A diagram of this django model as generated by [GraphViz:](http://www.graphviz.org/documentation/)
Diagram to come

## DJANGO-ADMIN: 
Found at the [/admin](https://opustm-api.herokuapp.com/admin) route of the API. After logging into an admin account, a site administrator can easily manage the database tables without the need to write any SQL. Read more [here](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
  
## JWT: 
Alongside Django REST we also use JSON-Web Token authentication for secure data transfer. We decided to implement this because it has been an IETF standard in the defined by the [RFC7519](https://tools.ietf.org/html/rfc7519) since 2015. 

## CORS/CSRF: 
We set up a white-list to only allow certain clients make requests to the API. This helps to make sure that only our React app will have access to the database.
