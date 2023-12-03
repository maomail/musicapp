from django import forms
from django.contrib.auth.forms import AuthenticationForm
from main.models import Song, Playlist

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'simple-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'simple-input'}))

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
        labels = {
            "name": "Название",
            "text": "Текст",
            "page_cover": "Обложка страницы",
            'song_cover': 'Обложка плеера',
            'notes': 'Ноты',
            'audio_file': 'Файл песни',
            'section': 'Настроение',
            'playlist': 'Плейлист',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'simple-input'}),
            'playlist': forms.SelectMultiple(attrs={'class': 'simple-input'}),
        }

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = "__all__"
        labels = {
            "name": "Название",
            "icon": "Картинка",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'simple-input'}),
        }
