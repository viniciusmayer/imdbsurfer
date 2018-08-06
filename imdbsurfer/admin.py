from django.contrib import admin
from django.utils.html import format_html
from imdbsurfer.models import Movie, Role, Artist, Genre, MovieGenre, MovieArtistRole, \
    Type


class MovieArtistRoleAdmin(admin.ModelAdmin):
    list_display = ('movie', 'getIMDbLink', 'getMovieRate', 'getArtistName', 'getRoleName')
    list_filter = ['artistRole__role__name']
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

class TypeFilter(admin.SimpleListFilter):
    title = ('_type')
    parameter_name = '_type'

    def lookups(self, request, model_admin):
        types = Type.objects.all()
        vtypes = []
        for _type in types:
            vtypes.append((str(_type.id), _type.name))
        return vtypes

    def queryset(self, request, queryset):
        if self.value() is not None:
            print(self.value())
            return queryset.filter(moviegenre__in=MovieGenre.objects.filter(type__id=self.value())).distinct()
        return queryset.all()

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'getIMDbLink', 'rate', 'metascore', 'minutes', 'votes', 'index', 'types', '_genres')
    list_filter = ['genres', TypeFilter]
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
