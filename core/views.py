from django.shortcuts import render
from core.models import Movie, Genre, Actor
from django.views.generic import DetailView, ListView


class HomeList(ListView):
    model = Movie
    template_name = 'core/index.html'


class GenreList(HomeList):

    def get(self, request, *args, **kwargs):
        self.queryset = Movie.objects.filter(
            genre=Genre.objects.get(**self.kwargs)
        )
        return super(GenreList, self).get(request, *args, **kwargs)


class ActorList(HomeList):

    def get(self, request, *args, **kwargs):
        self.queryset = Movie.objects.filter(
            actor=Actor.objects.get(**self.kwargs)
        )
        return super(ActorList, self).get(request, *args, **kwargs)


class MovieDetail(DetailView):
    model = Movie
    template_name = 'core/detail.html'
