def make_album(artist, album, songs=None):
    music_album = {'artist_name': artist, 'album_name': album, }
    if songs:
        music_album['songs'] = songs
    return music_album


while True:
    print("press q to exit")
    name_artist = input("Enter the name of artist: ")
    if name_artist == 'q':
        break
    name_album = input("Enter the name of album: ")
    if name_album == 'q':
        break
    break


music = make_album(name_artist, name_album)
print(music)