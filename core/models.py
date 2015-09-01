# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Movie(models.Model):
    title = models.CharField(_(u'Título'), max_length=100)
    resume = models.TextField(_('Sinopse'))
    slug = models.SlugField(_('Slug'))
    genre = models.ForeignKey('Genre', verbose_name=_(u'Gênero'))
    actor = models.ManyToManyField('Actor', verbose_name=_(u'Ator'))

    def __unicode__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(_(u'Gênero'), max_length=80)
    slug = models.SlugField(_('Slug'))

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(_(u'Gênero'), max_length=80)
    picture = models.ImageField(_('Imagem'))
    slug = models.SlugField(_('Slug'))

    def __unicode__(self):
        return self.name

