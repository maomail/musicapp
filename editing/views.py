from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserLoginForm, SongForm, PlaylistForm
from django.contrib.auth import login
from main.models import Song, Playlist
from django.db.models import Q

class SighinView(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'editing/signin.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('songlist')
        return render(request, 'editing/signin.html', context={'form': form})

class SongListView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            query = request.GET.get('q', '')
            songs = Song.objects.filter(Q(name__icontains=query))
            playlists = Playlist.objects.all()
            return render(request, 'editing/songlist.html', context={'songs': songs,'playlists': playlists})
        else:
            return redirect('signin')

class CreateView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            form = SongForm()
            return render(request, 'editing/editing.html', {'form': form})
        else:
            return redirect('signin')

    def post(self, request, *args, **kwargs):
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')

        return render(request, 'editing/editing.html', {'form': form})

class CreatePlaylistView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            form = PlaylistForm()
            return render(request, 'editing/playlist-editing.html', {'form': form})
        else:
            return redirect('signin')

    def post(self, request, *args, **kwargs):
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')

        return render(request, 'editing/playlist-editing.html', {'form': form})

class EditView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            song = get_object_or_404(Song.objects.all(), id=kwargs['id'])
            form = SongForm(instance=song)
            return render(request, 'editing/editing.html', {'form': form, 'song': song})
        else:
            return redirect('signin')

    def post(self, request, *args, **kwargs):
        song = get_object_or_404(Song.objects.all(), id=kwargs['id'])
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('main')
        return render(request, 'editing/editing.html', {'form': form, 'song': song})

class DeleteView(View):
    def post(self, request, *args, **kwargs):
        song = get_object_or_404(Song.objects.all(), id=kwargs['id'])
        song.delete()
        return redirect('songlist')



