def make_album(artist, album, songs=None):
    music_album = {'artist_name': artist, 'album_name': album, }
    if songs:
        music_album['songs'] = songs
    return music_album


music = make_album('dsp', 'aarya', songs=6)
print(music)