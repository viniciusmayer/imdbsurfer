from django.contrib import admin

from imdbsurfer.models import Movie, Role, Artist, Genre, ArtistRole

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'index', 'rate', 'metascore', 'minutes', 'votes', 'show_link', 'obs')
    list_filter = ['year', 'index', 'rate', 'metascore']
    search_fields = ['name', 'obs']
    
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