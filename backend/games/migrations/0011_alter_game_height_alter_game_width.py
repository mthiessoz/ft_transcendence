# Generated by Django 4.2.9 on 2024-02-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_game_height_game_pad_height_game_pad_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='height',
            field=models.FloatField(default=800),
        ),
        migrations.AlterField(
            model_name='game',
            name='width',
            field=models.FloatField(default=600),
        ),
    ]
