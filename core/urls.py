# coding: utf-8
from django.conf.urls import patterns, url
from core.views import MovieDetail, HomeList

urlpatterns = patterns(
    'core.views',
    url(r'^$', HomeList.as_view(), name='home'),
    url(r'^filme/(?P<slug>[\w-]+)/$', MovieDetail.as_view(), name='movie_detail'),
    url(r'^genero/(?P<slug>[\w-]+)/$', 'genre_item', name='genre_item'),
    url(r'^ator/(?P<slug>[\w-]+)/$', 'actor_item', name='actor_item'),
)
