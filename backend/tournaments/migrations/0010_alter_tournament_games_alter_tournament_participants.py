# Generated by Django 4.2.9 on 2024-02-14 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0019_alter_game_ball_x_alter_game_ball_y_and_more'),
        ('tournaments', '0009_alter_tournament_games_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='tournaments', to='games.game'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='tournaments', to=settings.AUTH_USER_MODEL),
        ),
    ]
