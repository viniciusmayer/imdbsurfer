# -*- coding: utf-8 -*-
from common.models import CommonInfo, Common 
from django.db import models


class Role(CommonInfo):
    def __str__(self):
        return self.name

class Artist(CommonInfo):
    role = models.ManyToManyField(Role, through='ArtistRole')

    def __str__(self):
        return self.name

class Type(CommonInfo):
    def __str__(self):
        return self.name
    
class Genre(CommonInfo):
    def __str__(self):
        return self.name

class ArtistRole(Common):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Movie(CommonInfo):
    year = models.PositiveSmallIntegerField()
    index = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    votes = models.PositiveIntegerField()
    link = models.CharField(max_length=255)
    minutes = models.PositiveSmallIntegerField(null=True)
    metascore = models.PositiveSmallIntegerField(null=True)
    watched = models.BooleanField(default=False)
    watch = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre, through='MovieGenre')
    artists = models.ManyToManyField(ArtistRole, through='MovieArtistRole')

    class Meta:
        ordering = ['-index', '-year']
    
    def __str__(self):
        return '{0} ({1})'.format(self.name, self.year)
    
    def types(self):
        types = Type.objects.filter(moviegenre__in=MovieGenre.objects.filter(movie=self)).distinct()
        tnames = []
        for _type in types:
            tnames.append(_type.name)
        return tnames
    
    def _genres(self):
        gnames = []
        for genre in self.genres.all():
            gnames.append(genre.name)
        return gnames

class MovieGenre(Common):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(null=True)

class MovieArtistRole(Common):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    artistRole = models.ForeignKey(ArtistRole, on_delete=models.CASCADE)
