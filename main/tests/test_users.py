from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

# import pdb
# pdb.set_trace()


class TestUserSetUp(APITestCase):
    """ Setup Declarations """

    def setUp(self):
        self.fake = Faker()
        self.users_url = "/users/"
        self.register_url = "/register/"
        self.user_by_userid = lambda x: f"/users/{x}/"
        self.get_teams_by_userid = lambda x: f"/users/{x}/teams/"
        self.get_contacts_by_userid = lambda x: f"/users/{x}/contacts/"
        self.get_schedule_by_userid = lambda x: f"/users/{x}/schedule/"
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
        self.user_data_invalid = {
            "username": self.fake.email().split("@")[0],
            "first_name": self.fake.name()[0],
            "last_name": self.fake.name()[1],
            "email": self.fake.email(),
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestUsers(TestUserSetUp):
    def post(self):
        self.client.post(self.register_url, self.user_data, format="json")

    # /users/
    def test_users_get(self):
        self.post()
        res = self.client.get(self.users_url)
        self.assertEqual(res.status_code, 200)

    def test_users_post(self):
        res = self.client.post(self.users_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_users_put(self):
        response = self.client.put(self.users_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_users_delete(self):
        response = self.client.put(self.users_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)

    # /register/
    def test_users_register_get(self):
        res = self.client.get(self.register_url)
        self.assertEqual(res.status_code, 405)

    def test_users_register_post(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["username"], self.user_data["username"])
        self.assertEqual(res.data["first_name"], self.user_data["first_name"])
        self.assertEqual(res.data["last_name"], self.user_data["last_name"])
        self.assertEqual(res.data["email"], self.user_data["email"])

        res = self.client.post(self.register_url, self.user_data_invalid, format="json")
        self.assertEqual(res.status_code, 400)

    def test_users_register_put(self):
        response = self.client.put(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_users_register_delete(self):
        response = self.client.delete(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)

    # /users/{userid}/
    def test_user_by_id_get(self):
        self.post()
        res = self.client.get(self.user_by_userid(1))
        self.assertEqual(res.status_code, 200)

    def test_user_by_id_post(self):
        res = self.client.post(self.user_by_userid(1), self.user_data, format="json")
        self.assertEqual(res.status_code, 405)

    def test_user_by_id_put(self):
        self.post()
        res = self.client.put(self.user_by_userid(1), self.user_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_user_by_id_delete(self):
        self.post()
        res = self.client.delete(self.user_by_userid(1))
        self.assertEqual(res.status_code, 204)

    # /users/{username}/teams/
    def test_user_teams_by_id_get(self):
        self.post()
        res = self.client.get(self.get_teams_by_userid(1))
        self.assertEqual(res.status_code, 200)

    def test_user_teams_by_id_post(self):
        res = self.client.post(
            self.get_teams_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(res.status_code, 405)

    def test_user_teams_by_id_put(self):
        response = self.client.put(
            self.get_teams_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_user_teams_by_id_delete(self):
        response = self.client.put(
            self.get_teams_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    # #/users/{username}/contacts
    def test_user_contcts_by_id_get(self):
        self.post()
        res = self.client.get(self.get_contacts_by_userid(1))
        self.assertEqual(res.status_code, 200)

    def test_user_contacts_by_id_post(self):
        res = self.client.post(
            self.get_contacts_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(res.status_code, 405)

    def test_user_contacts_by_id_put(self):
        response = self.client.put(
            self.get_contacts_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    def test_user_contacts_by_id_delete(self):
        response = self.client.put(
            self.get_contacts_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(response.status_code, 405)

    # /users/{username}/schedule
    def test_user_schedule_by_id_get(self):
        self.post()
        res = self.client.get(self.get_schedule_by_userid(1))
        self.assertEqual(res.status_code, 401)

    def test_user_schedule_by_id_post(self):
        res = self.client.post(
            self.get_schedule_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(res.status_code, 401)

    def test_user_schedule_by_id_put(self):
        response = self.client.put(
            self.get_schedule_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(response.status_code, 401)

    def test_user_schedule_by_id_delete(self):
        response = self.client.put(
            self.get_schedule_by_userid(1), self.user_data, format="json"
        )
        self.assertEqual(response.status_code, 401)
