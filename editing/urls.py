from django.urls import path, re_path
from . import views
from main.views import NotFoundView


urlpatterns = [
    path('signin/', views.SighinView.as_view(), name='signin'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('create-playlist/', views.CreatePlaylistView.as_view(), name='playlist-create'),
    path('create-playlist/<int:id>/', views.PlaylistEditView.as_view(), name='playlist-edit'),
    path('playlist-delete/<int:id>/', views.PlaylistDeleteView.as_view(), name='playlist-delete'),
    path('edit/<int:id>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:id>/', views.DeleteView.as_view(), name='delete'),
    path('', views.SongListView.as_view(), name='songlist'),
    re_path(r'^', NotFoundView.as_view(), name='not_found'),
]
