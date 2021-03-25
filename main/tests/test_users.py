from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestUserSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.users_url = "/users/"
        self.register_url = "/register/"
        self.get_teams_by_userid = "get_teams_by_userid"
        self.get_contacts_by_userid = "get_contacts_by_userid"
        self.get_schedule_by_userid = "get_schedule_by_userid"
        self.user_data={
            "username": "test",
            "first_name": "tes",
            "last_name": "t",
            "email": "test@example.com",
            "bio": "asdf",
            "picture": "asdf",
            "theme": "asdf",
            "phone": "asdf",
            "password":"asdf"
        }
        self.user_data_invalid = {
            "username":self.fake.email().split("@")[0],
            "first_name":self.fake.name()[0],
            "last_name":self.fake.name()[1],
            "email":self.fake.email()
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()


class TestUserViews(TestUserSetUp):
    #/users/
    def test_user_get(self):
        res=self.client.get(self.users_url)
        self.assertEqual(res.status_code, 200)

    def test_user_post(self):
        res=self.client.post(self.users_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_user_put(self):
        response=self.client.put(self.users_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_user_delete(self):
        response=self.client.put(self.users_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)

    #/register/
    def test_register_get(self):
        res=self.client.get(self.register_url)
        self.assertEqual(res.status_code, 405)

    def test_register_post(self):
        res=self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["username"], self.user_data["username"])
        self.assertEqual(res.data["first_name"], self.user_data["first_name"])
        self.assertEqual(res.data["last_name"], self.user_data["last_name"])
        self.assertEqual(res.data["email"], self.user_data["email"])

        res=self.client.post(self.register_url, self.user_data_invalid, format="json")
        self.assertEqual(res.status_code, 400)

    def test_register_put(self):
        response=self.client.put(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)

    def test_register_delete(self):
        response=self.client.put(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 405)






















    #/users/{username}
    # def test_user_get(self):
    #     res=self.client.get(self.users_url)
    #     self.assertEqual(res.status_code, 200)

    # def test_user_post(self):
    #     res=self.client.post(self.users_url, self.user_data, format="json")
    #     self.assertEqual(res.status_code, 201)

    # def test_user_put(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)

    # def test_user_delete(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)
    
    # #/users/{username}/teams
    # def test_user_get(self):
    #     res=self.client.get(self.users_url)
    #     self.assertEqual(res.status_code, 200)

    # def test_user_post(self):
    #     res=self.client.post(self.users_url, self.user_data, format="json")
    #     self.assertEqual(res.status_code, 201)

    # def test_user_put(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)

    # def test_user_delete(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)

    # #/users/{username}/contacts
    # def test_user_get(self):
    #     res=self.client.get(self.users_url)
    #     self.assertEqual(res.status_code, 200)

    # def test_user_post(self):
    #     res=self.client.post(self.users_url, self.user_data, format="json")
    #     self.assertEqual(res.status_code, 201)

    # def test_user_put(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)

    # def test_user_delete(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)

    # #/users/{username}/schedule
    # def test_user_get(self):
    #     res=self.client.get(self.users_url)
    #     self.assertEqual(res.status_code, 200)

    # def test_user_post(self):
    #     res=self.client.post(self.users_url, self.user_data, format="json")
    #     self.assertEqual(res.status_code, 201)

    # def test_user_put(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)

    # def test_user_delete(self):
    #     response=self.client.put(self.users_url, self.user_data, format="json")
    #     self.assertEqual(response.status_code, 405)