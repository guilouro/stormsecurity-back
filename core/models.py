# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Movie(models.Model):
    title = models.CharField(_(u'Título'), max_length=100)
    resume = models.TextField(_('Sinopse'))
    picture = models.ImageField(_('Imagem'))
    slug = models.SlugField(_('Slug'))
    genre = models.ForeignKey('Genre', verbose_name=_(u'Gênero'))
    actor = models.ManyToManyField('Actor', verbose_name=_(u'Ator'))

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('core:movie_detail', (), {'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = _('Filme')
        verbose_name_plural = _('Filmes')


class Genre(models.Model):
    name = models.CharField(_('Nome'), max_length=80)
    slug = models.SlugField(_('Slug'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Gênero')
        ordering = ['name']
        verbose_name_plural = _(u'Generos')


class Actor(models.Model):
    name = models.CharField(_('Nome'), max_length=80)
    picture = models.ImageField(_('Imagem'))
    slug = models.SlugField(_('Slug'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Ator')
        verbose_name_plural = _('Atores')
