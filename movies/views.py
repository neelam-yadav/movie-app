from django.shortcuts import redirect
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.views.generic import (
    ListView,
    CreateView,
)

from .forms import MovieForm, MovieSearchForm
from .models import Movie


# Create your views here.
class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm

    def form_valid(self, form):
        form.save()
        return redirect('Movie:list')


class MovieFilter(BaseFilter):
    search_fields = {
        'search_text': ['title'],
    }


class MovieSearchList(SearchListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 30
    template_name = "movies/movie_list.html"
    form_class = MovieSearchForm
    filter_class = MovieFilter
