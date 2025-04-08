from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='testuser@example.com', password='password123')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')

class TeamModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1', email='user1@example.com', password='password123')
        self.user2 = User.objects.create(username='user2', email='user2@example.com', password='password123')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user1, self.user2)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.members.count(), 2)

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='activityuser', email='activityuser@example.com', password='password123')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=timedelta(hours=1))

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, timedelta(hours=1))

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='leaderboarduser', email='leaderboarduser@example.com', password='password123')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout description')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.description, 'A test workout description')