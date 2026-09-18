from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import State, Season, Destinations, Restaurants

class GoaAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123', email='test@example.com')
        self.state = State.objects.create(state='Kerala')
        self.season = Season.objects.create(season='Honeymoon')
        self.destination = Destinations.objects.create(
            Title='Munnar Hills',
            Description='Beautiful tea gardens and hills in Munnar.',
            season=self.season,
            state=self.state
        )
        self.restaurant = Restaurants.objects.create(
            name='Grand Spice Hotel',
            price=2500,
            food='Kerala Seafood & Thali',
            state='Kerala'
        )

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_flow(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertRedirects(response, reverse('home'))

    def test_home_requires_login(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/login?next=/home')

    def test_search_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('search'), {'search': 'Munnar'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Munnar Hills')

    def test_state_filter_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('state', kwargs={'state1': 'Kerala'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Munnar Hills')

    def test_season_filter_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('honeymoon', kwargs={'season1': 'Honeymoon'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Munnar Hills')

    def test_destination_detail_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('readmore', kwargs={'id': self.destination.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Munnar Hills')

    def test_hotels_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('hotels'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grand Spice Hotel')
