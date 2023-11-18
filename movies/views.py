from django.http import HttpResponse
from .temp_data import movie_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Movie
from django.shortcuts import render, get_object_or_404
from django.views import generic 
from .models import Movie
from .forms import MovieForm

def detail_movie(request, movie_id): #controla o que aparece quando clicamos em um filme
    movie = Movie.objects.get(pk=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)




def search_movies(request):#search movies adaptada para a base de dados
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        movie_list = Movie.objects.filter(name__icontains=search_term)
        context = {"movie_list": movie_list}
    return render(request, 'movies/search.html', context)

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data['name']
            movie_release_year = form.cleaned_data['release_year']
            movie_poster_url = form.cleaned_data['poster_url']
            movie = Movie(name=movie_name,
                          release_year=movie_release_year,
                          poster_url=movie_poster_url)
            movie.save()
            return HttpResponseRedirect(
                reverse('movies:detail', args=(movie.id, )))
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/create.html', context)
    
'''def list_movies(request):#linka com a base de dados
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'movies/index.html', context)
'''
class MovieListView(generic.ListView):#genérica que substitui list_views
    model = Movie
    template_name = 'movies/index.html'

def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie.name = form.cleaned_data['name']
            movie.release_year = form.cleaned_data['release_year']
            movie.poster_url = form.cleaned_data['poster_url']
            movie.save()
            return HttpResponseRedirect(
                reverse('movies:detail', args=(movie.id, )))
    else:
        form = MovieForm(
            initial={
                'name': movie.name,
                'release_year': movie.release_year,
                'poster_url': movie.poster_url
            })

    context = {'movie': movie, 'form': form}
    return render(request, 'movies/update.html', context)

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        movie.delete()
        return HttpResponseRedirect(reverse('movies:index'))

    context = {'movie': movie}
    return render(request, 'movies/delete.html', context)