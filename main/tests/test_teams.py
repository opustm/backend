from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker 

class TestTeamsSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.teams_url = "/teams/"
        # self.get_members_by_userid = reverse("get_members_by_userid")
        self.team_data = {
            "id":1,
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

    def test_team_post(self):
        response=self.client.post(self.teams_url, self.team_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, self.team_data)

    def test_get_all_teams(self):
        res=self.client.get(self.teams_url)
        self.assertEqual(res.status_code, 200)

    # def test_get_team_by_teamid(self):
    #     response=self.client.get(f"{self.teams_url}/1")
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, {'members':[], 'managers':[], 'owners':[]})

    # def test_get_members_by_userid(self):
    #     response=self.client.get(self.teams_url)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, {'members':[], 'managers':[], 'owners':[]})