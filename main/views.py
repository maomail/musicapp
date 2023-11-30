from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Song, Section
from django.views.decorators.http import require_http_methods
from django.http import Http404

class IndexView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            funny_songs_count = Song.objects.filter(section__name='funny').count()
            sad_songs_count = Song.objects.filter(section__name='sad').count()
            beautiful_songs_count = Song.objects.filter(section__name='beautiful').count()
            context = {
                'funny_songs_count': funny_songs_count,
                'sad_songs_count': sad_songs_count,
                'beautiful_songs_count': beautiful_songs_count,
            }
            return render(request, 'main/index.html', context=context)
        else:
            return redirect('signin')

class SongView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            songs = Song.objects.filter(section__name=kwargs['section'])
            try:
                song = songs[kwargs['id']-1]
            except IndexError:
                return redirect('songlist')
            return render(request, 'main/song.html', context={'song': song})
        else:
            return redirect('signin')

class NotFoundView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            return render(request, 'main/not-found.html')
        else:
            return redirect('signin')


