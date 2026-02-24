from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        url = reverse('user-list')
        data = {"name": "Test User", "email": "test@example.com", "team": team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {"name": "Team Alpha"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="test@example.com", team=team)
        url = reverse('activity-list')
        data = {"user": user.id, "type": "run", "duration": 30, "date": "2024-01-01"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {"name": "Cardio Blast", "description": "Intenso", "suggested_for": "Todos"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Test Team")
        url = reverse('leaderboard-list')
        data = {"team": team.id, "points": 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
