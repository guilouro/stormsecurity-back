# coding: utf-8
from django.conf.urls import patterns, url
from core.views import MovieDetail, HomeList, GenreList, ActorList

urlpatterns = patterns(
    'core.views',
    url(r'^$', HomeList.as_view(), name='home'),
    url(r'^filme/(?P<slug>[\w-]+)/$', MovieDetail.as_view(), name='movie_detail'),
    url(r'^genero/(?P<slug>[\w-]+)/$', GenreList.as_view(), name='genre_list'),
    url(r'^ator/(?P<slug>[\w-]+)/$', ActorList.as_view(), name='actor_list'),
)
