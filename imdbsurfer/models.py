from django.db import models

from common.models import CommonInfo, Common 
from django.utils.html import format_html
    
class Role(CommonInfo):
    def __str__(self):
        return self.name

class Artist(CommonInfo):
    role = models.ManyToManyField(Role, through='ArtistRole')

    def __str__(self):
        return self.name
    
class Genre(CommonInfo):
    def __str__(self):
        return self.name

class ArtistRole(Common):
    artist = models.ForeignKey(Artist)
    role = models.ForeignKey(Role)

class Movie(CommonInfo):
    year = models.PositiveSmallIntegerField()
    index = models.PositiveSmallIntegerField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    votes = models.PositiveIntegerField()
    link = models.CharField(max_length=255)
    minutes = models.PositiveSmallIntegerField()
    metascore = models.PositiveSmallIntegerField(null=True)
    watched = models.BooleanField(default=False)
    watch = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre, through='MovieGenre')
    artists = models.ManyToManyField(ArtistRole, through='MovieArtistRole')
    
    def __str__(self):
        return '{0} ({1})'.format(self.name, self.year)

    def show_link(self):
        return  format_html('<a href="{0}" target="_blank">{1}</a>'.format(self.link, 'IMDb'))
    show_link.short_description = 'Link' 


class MovieGenre(Common):
    movie = models.ForeignKey(Movie)
    genre = models.ForeignKey(Genre)
    index = models.PositiveSmallIntegerField(null=True)
    
    def getImdbLink(self):
        return self.movie.show_link()
    getImdbLink.short_description = 'IMDb'

class MovieArtistRole(Common):
    movie = models.ForeignKey(Movie)
    artistRole = models.ForeignKey(ArtistRole)