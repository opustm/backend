from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestAnnouncementsSetUp(APITestCase):
    """ Setup Declarations """

    def setUp(self):
        self.fake = Faker()
        self.announcements_url = "/announcements/"
        self.announcements_by_id = lambda x: f"/announcements/{x}/"
        self.announcements_by_team_id = lambda x: f"/announcements/team/{x}/"
        self.announcements_by_user_id = lambda x: f"/announcements/user/{x}/"
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
        self.announcement_data = {
            "id": 1,
            "team": 1,
            "creator": 1,
            "priority": 1,
            "announcement": "hello world",
            "end": "2021-03-19T01:44:17.336000Z",
            "event": 1,
            "acknowledged": [],
        }
        self.announcement_data_invalid = {
            "team": "asdf",
            "creator": 10,
            "priority": 2,
            "announcement": "hello world",
            "end": "2021-03-19T01:44:17.336000Z",
            "event": 1,
            "acknowledged": [1],
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestAnnouncementsViews(TestAnnouncementsSetUp):
    def post(self):  # to post correctly we need to provide a valid user/team id.
        self.client.post("/users/", self.user_data, format="json")
        self.client.post("/teams/", self.team_data, format="json")
        self.client.post("/events/", self.event_data, format="json")
        self.client.post(self.announcements_url, self.announcement_data, format="json")

    def test_announcement_get(self):
        res = self.client.get(self.announcements_url)
        self.assertEqual(res.status_code, 200)

    def test_announcement_post(
        self,
    ):  # to post correctly we need to provide a valid user/team id.
        self.post()
        response = self.client.post(
            self.announcements_url, self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.announcement_data, self.announcement_data)

        response2 = self.client.post(
            self.announcements_url, self.announcement_data_invalid, format="json"
        )
        self.assertEqual(response2.status_code, 400)

    def test_announcement_put(self):
        response = self.client.put(
            self.announcements_url, self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_announcement_delete(self):
        response = self.client.delete(self.announcements_url)
        self.assertEqual(response.status_code, 405)

    # announcement_by_id
    def test_announcement_by_id_get(self):
        self.post()
        res = self.client.get(self.announcements_by_id(1))
        self.assertEqual(res.status_code, 200)

    def test_announcement_by_id_post(self):
        response = self.client.post(
            self.announcements_by_id(1), self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_announcement_by_id_put(self):
        self.post()
        response = self.client.put(
            self.announcements_by_id(1), self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_announcement_by_id_delete(self):
        self.post()
        response = self.client.delete(self.announcements_by_id(1))
        self.assertEqual(response.status_code, 204)

    # announcement_by_team_id
    def test_announcement_by_team_id_get(self):
        res = self.client.get(self.announcements_url)
        self.assertEqual(res.status_code, 200)

    def test_announcement_by_team_id_post(self):
        response = self.client.post(
            self.announcements_by_team_id(1), self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_announcement_by_team_id_put(self):
        response = self.client.put(
            self.announcements_by_team_id(1), self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_announcement_by_team_id_delete(self):
        response = self.client.delete(self.announcements_by_team_id(1))
        self.assertEqual(response.status_code, 405)

    # announcement_by_user_id
    def test_announcement_by_user_id_get(self):
        res = self.client.get(self.announcements_url)
        self.assertEqual(res.status_code, 200)

    def test_announcement_by_user_id_post(self):
        response = self.client.post(
            self.announcements_by_user_id(1), self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_announcement_by_user_id_put(self):
        response = self.client.put(
            self.announcements_by_user_id(1), self.announcement_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_announcement_by_user_id_delete(self):
        response = self.client.delete(self.announcements_by_user_id(1))
        self.assertEqual(response.status_code, 405)
