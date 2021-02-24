from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestUserSetUp(APITestCase):
    """ Setup Declarations """
    def setUp(self):
        self.fake = Faker()
        self.register_url = "/users/"
        self.register_url_alternate = "/register"
        self.get_teams_by_userid = "get_teams_by_userid"
        self.get_contacts_by_userid = "get_contacts_by_userid"
        self.get_schedule_by_userid = "get_schedule_by_userid"
        self.user_data = {
            "username":self.fake.email().split("@")[0],
            "first_name":self.fake.name()[0],
            "last_name":self.fake.name()[1],
            "email":self.fake.email()
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()


class TestUserViews(TestUserSetUp):
    def test_user_cannot_register_with_no_data(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res=self.client.post(
            self.register_url, self.user_data, format="json"
        )
        self.assertEqual(res.data["username"], self.user_data["username"])
        self.assertEqual(res.data["first_name"], self.user_data["first_name"])
        self.assertEqual(res.data["last_name"], self.user_data["last_name"])
        self.assertEqual(res.data["email"], self.user_data["email"])
        self.assertEqual(res.status_code, 201)

    # def test_user_cannot_register_with_no_data_with_alternate_url(self):
    #     res=self.client.post(self.register_url_alternate)
    #     self.assertEqual(res.status_code, 400)

    # def test_user_can_register_correctly_with_alternate_url(self):
    #     res=self.client.post(
    #         self.register_url_alternate, self.user_data, format="json"
    #     )
    #     self.assertEqual(res.data["username"], self.user_data["username"])
    #     self.assertEqual(res.data["first_name"], self.user_data["first_name"])
    #     self.assertEqual(res.data["last_name"], self.user_data["last_name"])
    #     self.assertEqual(res.data["email"], self.user_data["email"])
    #     self.assertEqual(res.status_code, 201)

    def test_user_can_get_all_users(self):
        # Create a series of new users and test they are formatted properly
        # TODO: Clear the database here somehow
        generated_users=[]
        for i in range(10):
            generated_users.append({
            "username":f"uname{i}", 
            "first_name":f"firstname{i}",
            "last_name":f"lastname{i}",
            "email":f"{i}@email.org",})
        res_array = []
        for user in generated_users:
            res_array.append(self.client.post(
                self.register_url, self.user_data, format="json"
            ))
        for user, res in zip(generated_users, res_array):
            self.assertEqual(res.data["username"], user["username"])
            self.assertEqual(res.data["first_name"], user["first_name"])
            self.assertEqual(res.data["last_name"], user["last_name"])
            self.assertEqual(res.data["email"], user["email"])
        # Get all the users and test all users are received properly
        get_res = self.client.get()
        for user, res in zip(generated_users, get_res.data):
            self.assertEqual(user["username"], res["username"])
            self.assertEqual(user["first_name"], res["first_name"])
            self.assertEqual(user["last_name"], res["last_name"])
            self.assertEqual(user["email"], res["email"])
            

    # def test_user_can_get_user_by_username(self):
        # res=
    
# class TestUserModel(TestUserSetUp):
    # def test_user_cannot_register_correctly_with_invalid_data(self):
        # invalid_data=self.user_data["u"]