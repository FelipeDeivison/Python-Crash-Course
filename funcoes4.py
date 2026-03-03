
def make_album(album, artista, total_musicas= None):
    album_music = {
        'Álbum': album,
        'Artista': artista,
        }
    if total_musicas:
        album_music['Músicas'] = total_musicas

    return album_music


print(make_album('MSB', 'Karol G'))
print(make_album('MSB', 'Karol G', 32))

