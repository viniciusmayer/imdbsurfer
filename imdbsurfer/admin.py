from django.contrib import admin

from imdbsurfer.models import Movie, Role, Artist, Genre, ArtistRole, MovieGenre, MovieArtistRole
from django.utils.html import format_html

class MovieArtistRoleAdmin(admin.ModelAdmin):
    list_display = ('movie', 'getMovieRate', 'getArtistName', 'getRoleName', 'getIMDbLink')
    list_filter = ['artistRole__artist__name']
    search_fields = ['movie__name', 'artistRole__artist__name']
    
    def getMovieRate(self, obj):
        return obj.movie.rate
    getMovieRate.short_description = 'Rate'
    
    def getArtistName(self, obj):
        return obj.artistRole.artist.name
    getArtistName.short_description = 'Artist'

    def getRoleName(self, obj):
        return obj.artistRole.role.name 
    getRoleName.short_description = 'Role'    

    def getIMDbLink(self, obj):
        return format_html('<a href="{0}" target="_blank">{1}</a>'.format(obj.movie.link, 'IMDb'))
    getIMDbLink.short_description = 'IMDb'

    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(MovieArtistRoleAdmin, self).save_model(request, obj, form, change)

admin.site.register(MovieArtistRole, MovieArtistRoleAdmin)

class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('movie', 'getIMDbLink', 'getMovieRate', 'genre', 'type', 'index')
    list_filter = ['genre__name', 'type__name', 'index']
    search_fields = ['movie__name']

    def getMovieRate(self, obj):
        return obj.movie.rate
    getMovieRate.short_description = 'Rate'
    
    def getIMDbLink(self, obj):
        return format_html('<a href="{0}" target="_blank">{1}</a>'.format(obj.movie.link, 'IMDb'))
    getIMDbLink.short_description = 'IMDb' 


    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(MovieGenreAdmin, self).save_model(request, obj, form, change)

admin.site.register(MovieGenre, MovieGenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'rate', 'metascore', 'minutes', 'votes', 'getIMDbLink')
    search_fields = ['name']

    def getIMDbLink(self, obj):
        return format_html('<a href="{0}" target="_blank">{1}</a>'.format(obj.link, 'IMDb'))
    getIMDbLink.short_description = 'IMDb' 

    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(MovieAdmin, self).save_model(request, obj, form, change)

admin.site.register(Movie, MovieAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'obs')
    search_fields = ['name', 'obs']
    
    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(RoleAdmin, self).save_model(request, obj, form, change)
        
admin.site.register(Role, RoleAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'obs')
    search_fields = ['name', 'obs']
    
    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(ArtistAdmin, self).save_model(request, obj, form, change)
        
admin.site.register(Artist, ArtistAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'obs')
    search_fields = ['name', 'obs']
    
    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(GenreAdmin, self).save_model(request, obj, form, change)

admin.site.register(Genre, GenreAdmin)
