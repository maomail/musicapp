from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="main"),
    path('song/<str:section>/<int:id>/', views.SongView.as_view(), name="song"),
]
