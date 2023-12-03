from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="main"),
    path('song/<str:section>/<int:id>/', views.SongView.as_view(), name="song"),
    path('playlist-song/<int:playlist_id>/', views.PlaylistSongView.as_view(), name="playlist-song"),
    re_path(r'^', views.NotFoundView.as_view(), name='not_found'),
]
