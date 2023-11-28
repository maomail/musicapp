from django.shortcuts import render
from django.views import View

class IndexView(View):

    songs = [
        {'name': 'Браво - Нет предела', 'text': 'Hello world!', 'section': 'funny'},
        {'name': 'pyrokinesis - Богиня мечей', 'text': 'Hello world!', 'section': 'sad'},
        {'name': 'Sirius Eye', 'text': 'Hello world!', 'section': 'beautiful'},
    ]

    def get(self, request, *args, **kwargs):
        context = {
            'funny_songs_count': 1,
            'sad_songs_count': 1,
            'beautiful_songs_count': 1,
        }
        return render(request, 'main/index.html', context=context)


