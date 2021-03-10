from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker 

class TestTeamsSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.teams_url = "/teams/"
        self.get_members_by_userid = reverse("get_members_by_userid")
        self.team_data = {
            members=[]
            managers
         }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()