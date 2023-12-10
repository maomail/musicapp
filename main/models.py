from django.db import models
from PIL import Image

class Playlist(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='playlist-icon/', blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    B = 'bea'
    F = 'fun'
    S = 'sad'
    name = models.CharField(max_length=120)
    text = models.TextField(max_length=1500, blank=True)
    page_cover = models.ImageField(upload_to='page-covers/', blank=True)
    song_cover = models.ImageField(upload_to='song-covers/', blank=True)
    notes = models.ImageField(upload_to='notes', blank=True)
    playlist = models.ManyToManyField(Playlist, blank=True)
    audio_file = models.FileField(upload_to='audio/', blank=True)
    TYPES_CHOICES = [
        (B, 'Красивое'),
        (F, 'Весело'),
        (S, 'Грустно'),
    ]
    section = models.CharField(
        max_length=3,
        choices=TYPES_CHOICES,
        default=F
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
        if self.page_cover:
            img = Image.open(self.page_cover.path)

            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.page_cover.path)

        if self.song_cover:
            img = Image.open(self.song_cover.path)

            if img.height > 500 or img.width > 500:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.song_cover.path)
