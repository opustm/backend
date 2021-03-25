from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestEventsSetUp(APITestCase):
    """ Setup Declarations """

    def setUp(self):
        self.fake = Faker()
        self.events_url = "/events/"
        self.event_data = {
            "user": 1,
            "team": 1,
            "name": "",
            "start": 1,
            "end": 1,
            "details": "",
            "picture": "",
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
    def test_event_get(self):
        res = self.client.get(self.events_url)
        self.assertEqual(res.status_code, 200)

    def test_event_post(self):
        response = self.client.post(self.events_url, self.event_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.event_data, self.event_data)

        response2 = self.client.post(
            self.events_url, self.event_data_invalid, format="json"
        )
        self.assertEqual(response2.status_code, 400)

    def test_event_put(self):
        response = self.client.put(self.events_url, self.event_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_event_delete(self):
        response = self.client.put(self.events_url, self.event_data, format="json")
        self.assertEqual(response.status_code, 405)
