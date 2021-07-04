from django.contrib import admin
from django.utils.html import format_html

from imdbsurfer_webapp.models import Movie, MovieGenre, Type


class TypeFilter(admin.SimpleListFilter):
    title = '_type'
    parameter_name = '_type'

    def lookups(self, request, model_admin):
        types = Type.objects.all()
        vtypes = []
        for _type in types:
            vtypes.append((str(_type.id), _type.name))
        return vtypes

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(moviegenre__in=MovieGenre.objects.filter(type__id=self.value())).distinct()
        return queryset.all()


class IndexFilter(admin.SimpleListFilter):
    title = 'Index'
    parameter_name = '_index'

    def lookups(self, request, model_admin):
        return [('0', '9+')
            , ('1', '8+')
            , ('2', '7+')
            , ('3', '6+')
            , ('4', '8-9')
            , ('5', '7-8')
            , ('6', '6.5-7')
            , ('7', '6-6.5')]

    def queryset(self, request, queryset):
        if self.value() is not None:
            if self.value() == '0':
                return queryset.filter(index__gte=9.00)
            elif self.value() == '1':
                return queryset.filter(index__gte=8.00)
            elif self.value() == '2':
                return queryset.filter(index__gte=7.00)
            elif self.value() == '3':
                return queryset.filter(index__gte=6.00)
            elif self.value() == '4':
                return queryset.filter(index__gte=8.00).filter(index__lt=9.00)
            elif self.value() == '5':
                return queryset.filter(index__gte=7.00).filter(index__lt=8.00)
            elif self.value() == '6':
                return queryset.filter(index__gte=6.50).filter(index__lt=7.00)
            elif self.value() == '7':
                return queryset.filter(index__gte=6.00).filter(index__lt=6.50)
        else:
            return queryset.all()


class LastUpdateFilter(admin.SimpleListFilter):
    title = 'Last update'
    parameter_name = '_last_update'

    def lookups(self, request, model_admin):
        return [('1', '> 0'), ('0', '< 0')]

    def queryset(self, request, queryset):
        if self.value() is not None:
            if self.value() == '0':
                return queryset.filter(last_update__lt=0)
            elif self.value() == '1':
                return queryset.filter(last_update__gt=0)
        return queryset.all()


def watched(modeladmin, request, queryset):
    for q in queryset:
        q.watched = True
        q.save()
    pass


watched.short_description = 'Marcar como assistido'


class MovieAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'year', 'getIMDbLink', 'rate', 'metascore', 'minutes', 'votes', 'index', 'types', '_genres', 'last_update')
    list_filter = ['watched', 'genres', TypeFilter, LastUpdateFilter, IndexFilter]
    search_fields = ['name']
    actions = [watched, ]

    def getIMDbLink(self, obj):
        return format_html('<a href="{0}" target="_blank">{1}</a>'.format(obj.link, 'IMDb'))

    getIMDbLink.short_description = 'IMDb'

    def save_model(self, request, obj, form, change):
        obj.user_create = request.user
        obj.user_update = request.user
        super(MovieAdmin, self).save_model(request, obj, form, change)


admin.site.register(Movie, MovieAdmin)
