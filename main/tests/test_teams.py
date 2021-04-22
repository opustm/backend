from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestTeamsSetUp(APITestCase):
    """ Setup Declarations """

    def setUp(self):
        self.fake = Faker()
        self.teams_url = "/teams/"
        self.team_by_id = lambda x: f"/teams/{x}/"
        self.team_members_by_id = lambda x: f"/teams/{x}/members/"
        # self.get_members_by_userid = reverse("get_members_by_userid")
        self.team_data = {
            "id": 1,
            "members": [],
            "managers": [],
            "owners": [],
            "name": "team",
            "workspace": "Luther",
            "teamType": "sub",
            "picture": "team.jpg",
            "displayName": "team",
            "description": "team",
            "permissions": [],
            "relatedteams": [],
        }
        self.team_data_invalid = {
            "id": 2,
            "members": [],
            "managers": [],
            "owners": [],
            "name": "fail",
            "workspace": "Luther",
            "teamType": "SUB",
            "picture": "fail.jpg",
            "displayName": "fail",
            "description": "fail",
            "permissions": [],
            "relatedteams": [],
        }
        self.team_data_change = {
            "id": 1,
            "members": [],
            "managers": [],
            "owners": [],
            "name": "team",
            "workspace": "Luther",
            "teamType": "sub",
            "picture": "updatedteam.jpg",
            "displayName": "team",
            "description": "team",
            "permissions": [],
            "relatedteams": [],
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestTeamsViews(TestTeamsSetUp):
    def post(self):
        self.client.post(self.teams_url, self.team_data, format="json")

    def test_team_get(self):
        res = self.client.get(self.teams_url)
        self.assertEqual(res.status_code, 200)

    def test_team_post(self):
        response = self.client.post(self.teams_url, self.team_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, self.team_data)

        response2 = self.client.post(
            self.teams_url, self.team_data_invalid, format="json"
        )
        self.assertEqual(response2.status_code, 400)

    def test_team_put(self):
        response = self.client.put(self.teams_url, self.team_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_team_delete(self):
        response = self.client.put(self.teams_url, self.team_data, format="json")
        self.assertEqual(response.status_code, 405)

    # /teams/{team_id}
    def test_team_by_id_get(self):
        self.post()
        res = self.client.get(self.team_by_id(1))
        self.assertEqual(res.status_code, 200)

    def test_team_by_id_post(self):
        response = self.client.post(self.team_by_id(1), self.team_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_team_by_id_put(self):
        self.post()
        response = self.client.put(self.team_by_id(1), self.team_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_team_by_id_delete(self):
        self.post()
        response = self.client.delete(self.team_by_id(1))
        self.assertEqual(response.status_code, 204)

    # /teams/{team_id}/members
    def test_team_members_by_id_get(self):
        self.post()
        res = self.client.get(self.team_members_by_id(1))
        self.assertEqual(res.status_code, 404)

    def test_team_members_by_id_post(self):
        response = self.client.post(
            self.team_members_by_id(1), self.team_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_team_team_members_by_id_put(self):
        response = self.client.put(
            self.team_members_by_id(1), self.team_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_team_members_by_id_delete(self):
        response = self.client.delete(self.team_members_by_id(1))
        self.assertEqual(response.status_code, 405)
