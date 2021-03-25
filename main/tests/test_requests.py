from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestRequestsSetUp(APITestCase):
    """ Setup Declarations """

    def setUp(self):
        self.fake = Faker()
        self.requests_url = "/requests/"
        self.request_data = {"message": "", "dateRequested": "1234"}
        self.request_data_invalid = {"message": "hello", "dateRequested": "1234"}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestRequestsViews(TestRequestsSetUp):
    def test_request_get(self):
        res = self.client.get(self.requests_url)
        self.assertEqual(res.status_code, 200)

    def test_request_post(self):
        response = self.client.post(self.requests_url, self.request_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.request_data, self.request_data)

        response2 = self.client.post(
            self.requests_url, self.request_data_invalid, format="json"
        )
        self.assertEqual(response2.status_code, 400)

    def test_request_put(self):
        response = self.client.put(self.requests_url, self.request_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_request_delete(self):
        response = self.client.put(self.requests_url, self.request_data, format="json")
        self.assertEqual(response.status_code, 405)
