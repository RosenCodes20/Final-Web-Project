from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from football_team_manager.schemes.models import Scheme

UserModel = get_user_model()
class TestSchemeViews(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        self.credentials = {
            'scheme': '4-3-3',
            'user': self.user
        }


    def test_create_scheme_view_works_correct(self):

        self.client.login(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        response = self.client.post(reverse('create-scheme'), self.credentials)

        self.assertEqual(Scheme.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Scheme.objects.filter(user=self.user).first(), Scheme.objects.last())


    def test_create_scheme_view_redirects_to_index(self):
        self.client.login(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        response = self.client.post(reverse('create-scheme'), self.credentials)

        self.assertRedirects(response, reverse('index'))