from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Song, Section
from django.views.decorators.http import require_http_methods
from django.http import Http404

songs = [
    {'name': 'Браво - Нет предела', 'text': 'Hello world!', 'section': 'funny'},
    {'name': 'pyrokinesis - Богиня мечей', 'text': 'Hello world!', 'section': 'sad'},
    {'name': 'Sirius Eye', 'text': 'Hello world!', 'section': 'beautiful'},
]

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'funny_songs_count': 1,
            'sad_songs_count': 1,
            'beautiful_songs_count': 1,
        }
        return render(request, 'main/index.html', context=context)

class SongView(View):

    def get(self, request, *args, **kwargs):
        songs = Song.objects.filter(section__name=kwargs['section'])
        try:
            song = songs[kwargs['id']-1]
        except IndexError:
            return redirect('main')
        return render(request, 'main/song.html', context={'song': song})



