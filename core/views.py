from django.db.models import Q
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

    def get_context_data(self, **kwargs):
        context_data = super(MovieDetail, self).get_context_data(**kwargs)
        related = Movie.objects.filter(
            Q(genre=self.object.genre) |
            Q(actor__name__in=list(self.object.actor.values_list('name', flat=True)))
        )[:10]
        context_data['related'] = related
        return context_data