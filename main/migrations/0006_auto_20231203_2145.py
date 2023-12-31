# Generated by Django 3.2.6 on 2023-12-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20231203_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='section',
        ),
        migrations.AddField(
            model_name='song',
            name='type',
            field=models.CharField(choices=[('btf', 'Красивое'), ('fun', 'Весело'), ('sad', 'Грустно')], default='fun', max_length=3),
        ),
        migrations.AddField(
            model_name='song',
            name='playlist',
            field=models.ManyToManyField(to='main.Playlist'),
        ),
    ]
