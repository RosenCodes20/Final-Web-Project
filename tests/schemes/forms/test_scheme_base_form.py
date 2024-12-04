from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from football_team_manager.schemes.forms import SchemeBaseForm
from football_team_manager.schemes.models import Scheme

UserModel = get_user_model()
class TestSchemeBaseForm(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='rosenivanov@gmail.com',
            password='12rosen34'
        )

        self.credentials = {
            'scheme': '4-3-3',
            'user': self.user
        }

    def test_form_is_valid_with_valid_credentials(self):
        form = SchemeBaseForm(data=self.credentials)

        self.assertTrue(form.is_valid())


    def test__form_returns_error_if_scheme_not_entered(self):
        self.credentials['scheme'] = ''

        form = SchemeBaseForm(data=self.credentials)

        self.assertFalse(form.is_valid())
        self.assertIn('scheme', form.errors)