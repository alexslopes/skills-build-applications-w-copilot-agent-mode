from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='test', team=team)
        self.assertEqual(user.email, 'test@test.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='test', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, calories=100)
        self.assertEqual(str(activity), 'test - run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='test', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=123)
        self.assertEqual(str(leaderboard), 'test: 123')
