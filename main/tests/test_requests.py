from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestRequestsSetUp(APITestCase):
    """ Setup Declarations """

    def setUp(self):
        self.fake = Faker()
        self.requests_url = "/requests/"
        self.requests_by_id = lambda x: f"/requests/{x}/"
        self.requests_by_team_id = lambda x: f"/requests/team/{x}/"
        self.requests_by_user_id = lambda x: f"/requests/user/{x}/"
        self.user_data = {
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
        self.request_data = {
            "user": 1,
            "team": 1,
            "message": "put me in coach",
            "dateRequested": "2021-03-29T13:53:50Z",
        }
        self.request_data_invalid = {"message": "hello", "dateRequested": "1234"}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestRequestsViews(TestRequestsSetUp):
    def post(self):
        self.client.post("/teams/", self.team_data, format="json")
        self.client.post("/users/", self.user_data, format="json")
        self.client.post("/events/", self.event_data, format="json")
        self.client.post(self.requests_url, self.request_data, format="json")

    # requests
    def test_request_get(self):
        res = self.client.get(self.requests_url)
        self.assertEqual(res.status_code, 200)

    def test_request_post(self):
        self.client.post("/teams/", self.team_data, format="json")
        self.client.post("/users/", self.user_data, format="json")
        self.client.post("/events/", self.event_data, format="json")
        response = self.client.post(self.requests_url, self.request_data, format="json")
        self.assertEqual(response.status_code, 201)

        invalid_response = self.client.post(
            self.requests_url, self.request_data_invalid, format="json"
        )
        self.assertEqual(invalid_response.status_code, 400)

    def test_request_put(self):
        response = self.client.put(self.requests_url, self.request_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_request_delete(self):
        response = self.client.delete(self.requests_url)
        self.assertEqual(response.status_code, 405)

    # requests by id
    def test_request_by_id_get(self):
        self.post()
        res = self.client.get(self.requests_by_id(1))
        self.assertEqual(res.status_code, 200)

    def test_request_by_id_post(self):
        response = self.client.post(
            self.requests_by_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_request_by_id_put(self):
        self.post()
        response = self.client.put(
            self.requests_by_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_request_by_id_delete(self):
        self.post()
        response = self.client.put(
            self.requests_by_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 200)

    # requests by team id
    def test_request_by_team_id_get(self):
        self.post()
        res = self.client.get(self.requests_by_team_id(1))
        self.assertEqual(res.status_code, 200)

    def test_request_by_team_id_post(self):
        response = self.client.post(
            self.requests_by_team_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_request_by_team_id_put(self):
        response = self.client.put(
            self.requests_by_team_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_request_by_team_id_delete(self):
        response = self.client.delete(
            self.requests_by_team_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    # requests by user id
    def test_request_by_user_id_get(self):
        self.post()
        res = self.client.get(self.requests_by_user_id(1))
        self.assertEqual(res.status_code, 200)

    def test_request_by_user_id_post(self):
        response = self.client.post(
            self.requests_by_user_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_request_by_user_id_put(self):
        response = self.client.put(
            self.requests_by_user_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_request_by_user_id_delete(self):
        response = self.client.delete(
            self.requests_by_user_id(1), self.request_data, format="json"
        )
        self.assertEqual(response.status_code, 405)
