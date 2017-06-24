from django.db import models

from common.models import CommonInfo, Common 

    
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

class MovieGenre(Common):
    movie = models.ForeignKey(Movie)
    genre = models.ForeignKey(Genre)

class MovieArtistRole(Common):
    movie = models.ForeignKey(Movie)
    artistRole = models.ForeignKey(ArtistRole)