from django.contrib import admin

from .models import Movie


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'synopsis', 'director')
    prepopulated_fields = {'slug': ('title',)}
