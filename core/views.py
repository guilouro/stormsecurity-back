from django.shortcuts import render
from core.models import Movie, Genre, Actor
from django.views.generic import DetailView

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, 'core/index.html', {'movies': movies})


class MovieDetail(DetailView):
    model = Movie
    template_name = 'core/detail.html'