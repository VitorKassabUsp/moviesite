from django.http import HttpResponse
from .temp_data import movie_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Movie
from django.shortcuts import render, get_object_or_404


def detail_movie(request, movie_id): #controla o que aparece ao clicar em cada filme
    movie = get_object_or_404(Movie, pk=movie_id)#contempla o caso de erro Not Found
    context = {'movie': movie_data[movie_id - 1]}
    return render(request, 'movies/detail.html', context)




def search_movies(request):#search movies adaptada para a base de dados
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        movie_list = Movie.objects.filter(name__icontains=search_term)
        context = {"movie_list": movie_list}
    return render(request, 'movies/search.html', context)

def create_movie(request): #create adaptado para a base de dados
    if request.method == 'POST':
        movie_name = request.POST['name']
        movie_release_year = request.POST['release_year']
        movie_poster_url = request.POST['poster_url']
        movie = Movie(name=movie_name,
                      release_year=movie_release_year,
                      poster_url=movie_poster_url)
        movie.save()
        return HttpResponseRedirect(
            reverse('movies:detail', args=(movie.id, )))
    else:
        return render(request, 'movies/create.html', {})
    
def list_movies(request):#linka com a base de dados
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'movies/index.html', context)
 