from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.
def home(request):
    # musicians = models.Musician.objects.all()
    albums = models.Album.objects.all()
    return render(request,"home.html", {'data': albums})


def add_music(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.MusicianForm()
    return render(request, 'add_music.html', {'form' : form})

def add_album(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form' : form})


def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id) 
    musician_form = forms.MusicianForm(instance=musician)

    if request.method == 'POST': 
        musician_form = forms.MusicianForm(request.POST, instance=musician) 
        if musician_form.is_valid(): 
            musician_form.save() 
            return redirect('homepage') 
    return render(request, 'add_music.html', {'form' : musician_form})


def edit_post(request, id):
    album = models.Album.objects.get(pk=id) 
    album_form = forms.AlbumForm(instance=album)

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save() 
            return redirect('homepage')
    
    return render(request, 'add_album.html', {'form' : album_form})



def delete_music(request, id):
    std = models.Album.objects.get(pk = id)
    std.delete()
    return redirect("homepage")