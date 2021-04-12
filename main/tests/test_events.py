from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestEventsSetUp(APITestCase):
    """ Setup Declarations """

    def setUp(self):
        self.fake = Faker()
        self.events_url = "/events/"
        self.event_by_id = lambda x: f"/events/{x}/"
        self.events_by_team_id = lambda x: f"/events/team/{x}/"
        self.events_by_user_id = lambda x: f"/events/user/{x}/"

        self.user_data = {
            "id": 1,
            "username": "test",
            "first_name": "tes",
            "last_name": "t",
            "email": "test@example.com",
            "bio": "asdf",
            "picture": "asdf",
            "theme": "asdf",
            "phone": "asdf",
            "password": "asdf",
        }
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
        self.event_data = {
            "id": 1,
            "user": 1,
            "team": 1,
            "name": "event",
            "start": "2021-03-29T13:25:34Z",
            "end": "2021-03-29T13:25:36Z",
            "details": "asdf",
            "picture": "asdf",
            "invited": [],
        }
        self.event_data_invalid = {
            "user": 2,
            "team": 1,
            "name": "",
            "start": 1,
            "end": 1,
            "details": "",
            "picture": "",
            "invited": [2],
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestEventsViews(TestEventsSetUp):
    def post(self):
        self.client.post("/teams/", self.team_data, format="json")
        self.client.post("/users/", self.user_data, format="json")
        self.client.post(self.events_url, self.event_data, format="json")

    def test_event_get(self):
        self.post()
        res = self.client.get(self.events_url)
        self.assertEqual(res.status_code, 200)

    def test_event_post(self):
        self.post()
        response = self.client.post(self.events_url, self.event_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.event_data, self.event_data)

        response2 = self.client.post(
            self.events_url, self.event_data_invalid, format="json"
        )
        self.assertEqual(response2.status_code, 400)

    def test_event_put(self):
        self.post()
        response = self.client.put(self.events_url, self.event_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_event_delete(self):
        self.post()
        response = self.client.delete(self.events_url, self.event_data, format="json")
        self.assertEqual(response.status_code, 405)

    # event_by_id
    def test_event_by_id_get(self):
        self.post()
        res = self.client.get(self.event_by_id(1))
        self.assertEqual(res.status_code, 200)

    def test_event_by_id_post(self):
        self.post()
        response = self.client.post(self.event_by_id(1), self.event_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_event_by_id_put(self):
        self.post()
        response = self.client.put(self.event_by_id(1), self.event_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_event_by_id_delete(self):
        self.post()
        response = self.client.delete(self.event_by_id(1))
        self.assertEqual(response.status_code, 204)

    # events_by_team_id
    def test_events_by_team_id_get(self):
        self.post()
        res = self.client.get(self.events_by_team_id(1))
        self.assertEqual(res.status_code, 200)

    def test_events_by_team_id_post(self):
        response = self.client.post(
            self.events_by_team_id(1), self.event_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_events_by_team_id_put(self):
        response = self.client.put(
            self.events_by_team_id(1), self.event_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_events_by_team_id_delete(self):
        response = self.client.delete(self.events_by_team_id(1))
        self.assertEqual(response.status_code, 405)

    # events_by_user_id
    def test_events_by_user_id_get(self):
        self.post()
        res = self.client.get(self.events_by_user_id(1))
        self.assertEqual(res.status_code, 200)

    def test_events_by_user_id_post(self):
        response = self.client.post(
            self.events_by_user_id(1), self.event_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_events_by_user_id_put(self):
        response = self.client.put(
            self.events_by_user_id(1), self.event_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_events_by_user_id_delete(self):
        response = self.client.delete(self.events_by_user_id(1))
        self.assertEqual(response.status_code, 405)
