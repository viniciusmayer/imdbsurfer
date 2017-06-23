from django.contrib import admin

from models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'index', 'rate', 'votes', 'link', 'obs')
    list_filter = ['year', 'index', 'rate']
    search_fields = ['name', 'obs']
    
    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(MovieAdmin, self).save_model(request, obj, form, change)

admin.site.register(Movie, MovieAdmin)