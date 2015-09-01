# coding: utf-8
from django.contrib import admin
from core.models import Movie, Genre, Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    prepopulated_fields = {'slug': ('title',)}

    def image(self, obj):
        return '<img src="/media/%s" width="50" alt="" />' % obj.picture

    image.allow_tags = True


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
