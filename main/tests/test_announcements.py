from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker 

class TestAnnouncementsSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.announcements_url = "/announcements/"
        self.get_team_announcements_by_teamid = reverse("get_team_announcements_by_teamid")
        self.get_user_announcements_by_userid = reverse("get_user_announcements_by_userid")
        self.team_data = { }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
