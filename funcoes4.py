
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

while True:
    print('DIgite informações sobre o álbum, caso queira sair basta digitar' \
    '"q".')
    album = input('Digite o nome do album que deseja adicionar: ')

    if album == 'q':
        break

    artista = input('Qual o nome do Artista? ')

    if artista == 'q':
        break

    musicas = input('Deseja adicionar o quantidade de músicas do album? '
    '(Responda com "s" para sim e "n" para não.)')

    if musicas == 'q':
        break

    if musicas == 's':
        total_musicas = int(input('Digite somente a quantidade de música no'
        'álbum'))
        album_criado = make_album(album, artista, total_musicas)
    else:
        album_criado = make_album(album, artista)

    print('álbum criado:\n')
    print(album_criado)