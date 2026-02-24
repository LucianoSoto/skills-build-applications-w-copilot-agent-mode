from django.core.management.base import BaseCommand
import random
from datetime import datetime, timedelta
from octofit_tracker.models import User, Team, Activity

# Populate the octofit_db database with test data

USERS = [
    {'name': 'Alice', 'email': 'alice@example.com', 'is_superhero': False},
    {'name': 'Bob', 'email': 'bob@example.com', 'is_superhero': True},
    {'name': 'Carol', 'email': 'carol@example.com', 'is_superhero': False},
    {'name': 'Dave', 'email': 'dave@example.com', 'is_superhero': False},
]

TEAMS = [
    {'name': 'Team Rocket', 'description': 'Equipo de velocidad'},
    {'name': 'Team Alpha', 'description': 'Equipo de fuerza'},
]

ACTIVITIES = [
    {'type': 'Running', 'duration': 30},
    {'type': 'Cycling', 'duration': 60},
    {'type': 'Swimming', 'duration': 45},
]

class Command(BaseCommand):
    help = 'Pobla la base de datos con datos de prueba para OctoFit Tracker'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creando equipos...')
        teams = self.create_teams()
        self.stdout.write('Creando usuarios...')
        users = self.create_users(teams)
        self.stdout.write('Creando actividades...')
        self.create_activities(users)
        self.stdout.write(self.style.SUCCESS('¡Datos de prueba creados exitosamente!'))

    def create_teams(self):
        team_objs = []
        for t in TEAMS:
            team, _ = Team.objects.get_or_create(name=t['name'], defaults={'description': t['description']})
            team_objs.append(team)
        return team_objs

    def create_users(self, teams):
        user_objs = []
        for idx, u in enumerate(USERS):
            team = teams[idx % len(teams)]
            user, _ = User.objects.get_or_create(
                name=u['name'],
                email=u['email'],
                team=team,
                is_superhero=u['is_superhero']
            )
            user_objs.append(user)
        return user_objs

    def create_activities(self, users):
        for user in users:
            for i in range(5):
                act = random.choice(ACTIVITIES)
                date = datetime.now().date() - timedelta(days=random.randint(0, 30))
                Activity.objects.create(
                    user=user,
                    type=act['type'],
                    duration=act['duration'],
                    date=date
                )
