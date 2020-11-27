from django.contrib import admin

# Register your models here.
from .models import Author, Book,MOVIE_DATA,MUSIC_DATA,SHOPING_DATA,GAME_DATA
admin.site.register(Author)
admin.site.register(Book)
class MovieAdd(admin.ModelAdmin):
    list_display = ['Name', 'link', 'show_image']
    fieldsets = (
        (None, {'fields': ['Name', 'link', 'image']}
        ),     
    )
class MusicAdd(admin.ModelAdmin):
    list_display = ['Name', 'link', 'show_image']
    fieldsets = (
        (None, {'fields': ['Name', 'link', 'image']}
        ),     
    )
class ShopAdd(admin.ModelAdmin):
    list_display = ['Name', 'link', 'show_image']
    fieldsets = (
        (None, {'fields': ['Name', 'link', 'image']}
        ),     
    )
class GameAdd(admin.ModelAdmin):
    list_display = ['Name', 'link', 'show_image']
    fieldsets = (
        (None, {'fields': ['Name', 'link', 'image']}
        ),     
    )
admin.site.register(MOVIE_DATA,MovieAdd)
admin.site.register(SHOPING_DATA,ShopAdd)
admin.site.register(MUSIC_DATA,MusicAdd)
admin.site.register(GAME_DATA,GameAdd)