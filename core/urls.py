# coding: utf-8
from django.conf.urls import patterns, url
from core.views import MovieDetail

urlpatterns = patterns(
    'core.views',
    url(r'^$', 'home', name='home'),
    url(r'^filme/(?P<slug>[\w-]+)/$', MovieDetail.as_view(), name='movie_detail'),
)
