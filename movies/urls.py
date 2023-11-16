from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.list_movies, name='index'),
    path('search/', views.search_movies, name='search'), # adicione esta linha
    path('<int:movie_id>/', views.detail_movie, name='detail'),
    path('create/', views.create_movie, name='create'), # adicione esta linha
]
