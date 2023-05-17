def make_album(artist, album, songCount=''):
    album = {
        'artist': artist.title(),
        'album title': album.title(),
    }

    if songCount:
        album['song count'] = songCount

    return album

distance = make_album("menual", "distance", 5)
night = make_album("perturbator", "i am the night", 15)
motorcycle_cop = make_album("power glove", "EP II")

print(distance)
print(night)
print(motorcycle_cop)