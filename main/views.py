from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Song, Playlist
import random

class IndexView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            funny_songs_count = Song.objects.filter(section__in='fun').count()
            sad_songs_count = Song.objects.filter(section__in='sad').count()
            beautiful_songs_count = Song.objects.filter(section__in='btf').count()
            playlists = Playlist.objects.all()
            context = {
                'funny_songs_count': funny_songs_count,
                'sad_songs_count': sad_songs_count,
                'beautiful_songs_count': beautiful_songs_count,
                'playlists': playlists
            }
            return render(request, 'main/index.html', context=context)
        else:
            return redirect('signin')

class SongView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            songs = Song.objects.filter(section=kwargs['section'])
            try:
                song = songs[kwargs['id']-1]
            except IndexError:
                return redirect('songlist')
            return render(request, 'main/song.html', context={'song': song})
        else:
            return redirect('signin')

class PlaylistSongView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            playlist_id = kwargs['playlist_id']
            songs = Song.objects.filter(playlist__pk=playlist_id)
            if songs.exists():
                rand_id = random.randint(1, songs.count())
                try:
                    song = songs[rand_id-1]
                except IndexError:
                    return redirect('songlist')
                return render(request, 'main/song.html', context={'song': song})
            else:
                return redirect('songlist')
        else:
            return redirect('signin')

class NotFoundView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            return render(request, 'main/not-found.html')
        else:
            return redirect('signin')


