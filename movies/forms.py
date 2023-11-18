from django.forms import ModelForm
from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = [
            'name',
            'release_year',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Data de Lançamento',
            'poster_url': 'URL do Poster',
        }