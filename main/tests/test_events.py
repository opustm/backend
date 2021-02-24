from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker 

class TestEventsSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.events_url = "/events/"
        self.get_team_events_by_teamid = reverse("get_team_events_by_teamid")
        self.get_user_events_by_userid = reverse("get_user_events_by_userid")
        self.event_data = { }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
