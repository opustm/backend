from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker 

class TestRequestsSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.requests_url = "/requests/"
        self.get_team_requests_by_teamid = reverse("get_team_requests_by_teamid")
        self.get_user_requests_by_username = reverse("get_user_requests_by_username")
        self.requests_data = { }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()