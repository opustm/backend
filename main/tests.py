from django.test import TestCase
from django.test import Client
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from main.models import *
import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .views import *

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testcase", first_name= "test", last_name="case", email="asdf@example.com", picture="pic", theme="theme2", phone="1234567897")

    def test_user_email(self):
        testuser= User.objects.get(username="testcase")
        self.assertEqual(testuser.usercode(), 'testcaseasdf@example.com')

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        data = {
            "username":"testcase", 
            "first_name": "test",
            "last_name":"case",
            "email":"asdf@example.com",
            "phone":"1234567897",
            "picture":"pic",
            "theme":"theme2",
            "teams": []
            }
        response = self.client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testcase')

    def test_get_user(self):
        """
        Ensure we can get object by username
        """
        response = self.client.get('/users/testcase/')
        self.assertEqual(response.data, {
            "username":"testcase", 
            "first_name": "test",
            "last_name":"case",
            "email":"asdf@example.com",
            "phone":"1234567897",
            "picture":"pic",
            "theme":"theme2",
            "teams": []
            })