from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker 

class TestAnnouncementsSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.announcements_url = "/announcements/"
        self.announcement_data = {
            "team": 1,
            "creator": 1,
            "priority": 1,
            "announcement": "hello world",
            "end": "2021-03-19T01:44:17.336000Z",
            "event": 1,
            "acknowledged": []
        }
        self.announcement_data_invalid = {
            "team": "asdf",
            "creator": 1,
            "priority": 2,
            "announcement": "hello world",
            "end": "2021-03-19T01:44:17.336000Z",
            "event": 1,
            "acknowledged": [1]
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

class TestAnnouncementsViews(TestAnnouncementsSetUp):
    def test_announcement_get(self):
        res=self.client.get(self.announcements_url)
        self.assertEqual(res.status_code, 200)

    def test_announcement_post(self):
        response=self.client.post(self.announcements_url, self.announcement_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.announcement_data, self.announcement_data)
        
        response2=self.client.post(self.announcements_url, self.announcement_data_invalid, format="json")
        self.assertEqual(response2.status_code, 400)

    def test_announcement_put(self):
        response=self.client.put(self.announcements_url, self.announcement_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_announcement_delete(self):
        response=self.client.put(self.announcements_url, self.announcement_data, format="json")
        self.assertEqual(response.status_code, 405)