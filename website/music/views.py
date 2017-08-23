from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', { "all_albums": all_albums })

def detail(request, album_id):
    album=get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.is_favourite = True
    song.save()
    return render(request, 'music/detail.html', {"album": song.album.id})
