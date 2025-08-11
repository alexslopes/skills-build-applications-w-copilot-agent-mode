from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Limpar dados existentes
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Criar times
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Criar usuários
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='cap', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', first_name='Clark', last_name='Kent', team=dc)

        # Criar atividades
        app_models.Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        app_models.Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        app_models.Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        app_models.Activity.objects.create(user=clark, type='run', duration=50, calories=450)

        # Criar treinos
        app_models.Workout.objects.create(name='Full Body', description='Treino completo para super-heróis')
        app_models.Workout.objects.create(name='Cardio Power', description='Cardio intenso para resistência')

        # Criar leaderboard
        app_models.Leaderboard.objects.create(user=tony, points=1000)
        app_models.Leaderboard.objects.create(user=steve, points=900)
        app_models.Leaderboard.objects.create(user=bruce, points=950)
        app_models.Leaderboard.objects.create(user=clark, points=1100)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
