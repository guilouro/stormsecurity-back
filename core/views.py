from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from core.models import Movie, Genre, Actor
from django.views.generic import DetailView, ListView


class HomeList(ListView):
    model = Movie
    template_name = 'core/index.html'


def genre_item(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    related = Movie.objects.filter(genre=genre)
    if 'order_by' in request.GET:
        related = related.order_by(request.GET['order_by'])
    return render(request, 'core/genre.html', {'genre': genre, 'related': related[:10]})


def actor_item(request, slug):
    actor = get_object_or_404(Actor, slug=slug)
    related = Movie.objects.filter(actor=actor)[:10]
    return render(request, 'core/actor.html', {'actor': actor, 'related': related})


class MovieDetail(DetailView):
    model = Movie
    template_name = 'core/detail.html'

    def get_context_data(self, **kwargs):
        context_data = super(MovieDetail, self).get_context_data(**kwargs)
        related = Movie.objects.filter(
            Q(genre=self.object.genre) |
            Q(actor__name__in=list(
                self.object.actor.values_list('name', flat=True)))
        ).exclude(id=self.object.id)[:10]
        context_data['related'] = related
        return context_data
