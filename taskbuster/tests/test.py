# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
from django.utils.translation import activate
from .views import home
from parameterized import parameterized


class HomeNewVisitorTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @parameterized.expand([
        ('en', '<h1>Welcome to TaskBuster!</h1>'),
        ('es', '<h1>Bienvenido a TaskBuster!</h1>'),
    ])
    def test_internationalization(self, lang, text):
        activate(lang)
        request = self.factory.get('/')
        response = home(request)
        # import ipdb; ipdb.set_trace()
        # self.assertEqual(response.status_code, 200)
        self.assertContains(response, text, html=True)
