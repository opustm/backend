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
            "name":"test team",
            "members":[],
            "managers":[],
            "owners":[],
            "description":"a test team",
            "displayName":"test",
            "picture":"test.jpg",
            "teamType":"SUB",
            "workspace":"general",
            "relatedTeams":[]
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

class TestTeamsViews(TestTeamsSetUp):
    def test_get_all_teams(self):
        res=self.client.get(self.teams_url)
        self.assertEqual(res.status_code, 400)

class TestTeamViews(TestTeamsSetUp):
    def test_get_all_teams(self):
        res=self.client.get(self.teams_url)
        self.assertEqual(res.status_code, 201)

class TestTeamMembersViews(TestTeamsSetUp):
    def test_get_all_teams(self):
        res=self.client.get(self.teams_url)
        self.assertEqual(res.status_code, 201)