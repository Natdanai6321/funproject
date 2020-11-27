from django.shortcuts import render, redirect
from .models import List,MOVIE_DATA,MUSIC_DATA,SHOPING_DATA,GAME_DATA
from .forms import ListForm
from django.http import HttpResponseRedirect

#Create your views here.
def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            allItems = List.objects.all
            return render(request, 'index.html', {'all' : allItems})
    else:
        allItems = List.objects.all
        return render(request, 'index.html', {'all' : allItems})
        
def about(request):
    return render (request, 'about.html')

def movie(request):
    allItems = MOVIE_DATA.objects.all
    return render (request, 'movie.html',{'all': allItems})

def music(request):
    allItems = MUSIC_DATA.objects.all
    return render (request, 'music.html',{'all': allItems})

def game(request):
    allItems = GAME_DATA.objects.all
    return render (request, 'game.html',{'all': allItems})

def shoping(request):
    allItems = SHOPING_DATA.objects.all
    return render (request, 'shoping.html',{'all': allItems})

def contact(request):
    return render (request, 'contact.html')

def delete(request, itemID):
    item = List.objects.get(pk=itemID)
    item.delete()
    return redirect ('index')

def complete(request, itemID):
    item = List.objects.get(pk=itemID)
    item.finished = True
    item.save()
    return redirect ('index')

def incomplete(request, itemID):
    item = List.objects.get(pk=itemID)
    item.finished = False
    item.save()
    return redirect ('index')

