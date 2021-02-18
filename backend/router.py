from main.viewsets import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teams', TeamViewset)
router.register('users', UserViewset)
router.register('invitations', InvitationViewset)
router.register('events', EventViewset)
router.register('schedules', ScheduleViewset)
router.register('timeFrames', TimeFrameViewset)
router.register('announcements', AnnouncementViewset)
# router.register('teamMessages', TeamMessageViewset)
# router.register('directMessages', DirectMessageViewset)
# router.register('reactions', ReactionViewset)
router.register('requests', RequestViewset)