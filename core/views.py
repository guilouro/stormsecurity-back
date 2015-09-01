from django.shortcuts import render
from core.models import Movie, Genre, Actor
from django.views.generic import DetailView, ListView


# def home(request):
#     if 'order_by' in request.GET:
#         movies = Movie.objects.all().order_by(request.GET['order_by'])
#     else:
#         movies = Movie.objects.all()
#     return render(request, 'core/index.html', {'movies': movies})


class HomeList(ListView):
    model = Movie
    template_name = 'core/index.html'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'core/detail.html'