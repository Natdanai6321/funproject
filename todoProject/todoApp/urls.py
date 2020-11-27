from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('movie/', views.movie, name='movie'),
    path('music/', views.music, name='music'),
    path('game/', views.game, name='game'),
    path('shoping/', views.shoping, name='shoping'),
    path('contact/', views.contact, name='contact'),
    path('delete/<itemID>', views.delete, name='delete'),
    path('complete/<itemID>', views.complete, name="complete"),
    path('incomplete/<itemID>', views.incomplete, name="incomplete"),
  
]