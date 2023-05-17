def make_album(artist, album, songCount=''):
    '''Create a dictionary of an album, containing the artist, album name, and optional song count.'''
    album = {
        'artist': artist.title(),
        'album title': album.title(),
    }

    if songCount:
        album['song count'] = songCount

    return album

print("Let's add some albums to your discography...")
while True:
    print("\nPlease enter the relevant album information: ")
    print("(enter 'quit' at any time to quit)")
    album_title = input("Album title: ")

    if album_title.lower() == 'quit':
        break

    album_artist = input("Artist: ")

    if album_artist.lower() == 'quit':
        break

    print("\nDo you know the song count? (yes/no)")
    song_count_flag = input()

    if song_count_flag.lower() == 'yes':
        song_count = input("Song count: ")
        album = make_album(album_artist, album_title, song_count)
    elif song_count_flag.lower() == 'quit':
        break
    else:
        album = make_album(album_artist, album_title)

    print(album)

