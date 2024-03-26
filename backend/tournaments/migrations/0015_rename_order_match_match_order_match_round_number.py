# Generated by Django 4.2.9 on 2024-02-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0014_remove_tournament_games_roundprogress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='order',
            new_name='match_order',
        ),
        migrations.AddField(
            model_name='match',
            name='round_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]