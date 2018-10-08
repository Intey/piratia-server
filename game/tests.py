from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class BattleCase(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create_user(username='admin', password='123123qwe')
        User.objects.create_user(username='test', password='123123qwe')
        self.c = Client()

    def test_start_battle(self):
        self.user1 = self.c.login(username='admin', password='123123qwe')
        response = self.c.post(reverse('search-battle'))
        self.assertEqual(response.status_code, 200, response.json())
        res = self.c.get(reverse('wait-for-battle'))
        self.assertEqual(res.status_code, 200, res.json())
        self.assertFalse(res.json()['ready'], res.json())

        self.user2 = self.c.login(username='test', password='123123qwe')
        response = self.c.post(reverse('search-battle'))
        self.assertEqual(response.status_code, 200, response.json())
        res = self.c.get(reverse('wait-for-battle'))
        self.assertEqual(res.status_code, 200, res.json())
        self.assertTrue(res.json()['ready'], res.json())
