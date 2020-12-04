from main.viewsets import TeamViewset, UserViewset, InvitationViewset, EventViewset, ScheduleTimeFrameViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teams', TeamViewset)
router.register('users', UserViewset)
router.register('invitations', InvitationViewset)
router.register('events', EventViewset)
router.register('scheduleTimeFrames', ScheduleTimeFrameViewset)
