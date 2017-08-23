from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', { "all_albums": all_albums })

def detail(request, album_id):
    album=get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
        print(selected_song)
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album, 'error_message': "You did now select valid song"})
    else:
        # if it reaches this, everythin worked fine until now
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
        