from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Sample data for superheroes
USERS = [
    {"username": "ironman", "email": "ironman@marvel.com", "team": "marvel"},
    {"username": "captainamerica", "email": "cap@marvel.com", "team": "marvel"},
    {"username": "spiderman", "email": "spiderman@marvel.com", "team": "marvel"},
    {"username": "batman", "email": "batman@dc.com", "team": "dc"},
    {"username": "superman", "email": "superman@dc.com", "team": "dc"},
    {"username": "wonderwoman", "email": "wonderwoman@dc.com", "team": "dc"},
]

TEAMS = [
    {"name": "marvel"},
    {"name": "dc"},
]

ACTIVITIES = [
    {"user": "ironman", "activity": "run", "distance": 5},
    {"user": "batman", "activity": "cycle", "distance": 10},
]

LEADERBOARD = [
    {"team": "marvel", "points": 100},
    {"team": "dc", "points": 90},
]

WORKOUTS = [
    {"name": "Pushups", "description": "Do 20 pushups"},
    {"name": "Situps", "description": "Do 30 situps"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Create unique index on email for users
        db.users.create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
