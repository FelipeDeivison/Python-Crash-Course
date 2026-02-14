favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

pessoas = ['jen', 'phil', 'lara', 'felipe']

for pessoa in pessoas:
    if pessoa in favorite_languages.keys():
        print(f'\nObrigado {pessoa} por responder a pesquisa!')
    else:
        print(f'\nOlá, {pessoa}! Tem uma pesquisa disponivel!')