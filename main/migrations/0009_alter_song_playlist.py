# Generated by Django 3.2.6 on 2023-12-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_type_song_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='playlist',
            field=models.ManyToManyField(blank=True, to='main.Playlist'),
        ),
    ]
