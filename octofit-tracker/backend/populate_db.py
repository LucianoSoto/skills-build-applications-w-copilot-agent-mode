
import os
import django
import random
from datetime import datetime, timedelta

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity

# --- Configuración de datos de prueba ---
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

# --- Creación de equipos ---
def create_teams():
    team_objs = []
    for t in TEAMS:
        team, _ = Team.objects.get_or_create(name=t['name'], defaults={'description': t['description']})
        team_objs.append(team)
    return team_objs

# --- Creación de usuarios ---
def create_users(teams):
    user_objs = []
    for idx, u in enumerate(USERS):
        # Asignar equipo alternando
        team = teams[idx % len(teams)]
        user, _ = User.objects.get_or_create(
            name=u['name'],
            email=u['email'],
            team=team,
            is_superhero=u['is_superhero']
        )
        user_objs.append(user)
    return user_objs

# --- Creación de actividades ---
def create_activities(users):
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

def main():
    print('Creando equipos...')
    teams = create_teams()
    print('Creando usuarios...')
    users = create_users(teams)
    print('Creando actividades...')
    create_activities(users)
    print('¡Datos de prueba creados exitosamente!')

if __name__ == '__main__':
    main()
