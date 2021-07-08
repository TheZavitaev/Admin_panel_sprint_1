from django.contrib import admin

from .models import FilmWork, FilmWorkPerson, Genre, Person


class PersonRoleInline(admin.TabularInline):
    model = FilmWorkPerson
    extra = 0


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type', 'rating')
    search_fields = ('title', 'description', 'id')

    fields = ('title', 'type', 'description', 'creation_date', 'certificate',
              'file_path', 'mpaa_rating', 'rating', 'genres')

    inlines = [PersonRoleInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birthdate')
    search_fields = ('full_name',)
