pessoa = {
    'first name': 'Felipe',
    'last name': 'Angelo',
    'age': '23',
    'city': 'Bela Cruz',
}
pessoa1 = {
    'first name': 'João',
    'last name': 'Angelo',
    'age': '31',
    'city': 'São Paulo',
}

pessoa2 = {
    'first name': 'Carlos',
    'last name': 'Angelo',
    'age': '28',
    'city': 'Fortaleza',
}

people = [pessoa, pessoa1, pessoa2]


for pessoas in people:
    print(
        f'\nNome: {pessoas['first name']}'
        f'\nSobrenome: {pessoas['last name']}'
        f'\nIdade: {pessoas['age']}' f'\tCidade: {pessoas['city']}'
        )
    
print('\n\tLista de Pets e seus donos\n')
    
cachorro = {
    'Pet:': 'Cachorro',
    'Raça:': 'Golden Retriever',
    'Dono:': 'Felipe Angelo',
}

gato = {
    'Pet:': 'Gato',
    'Raça:': 'Siamês',
    'Dono:': 'Natiara Angelo',
}

passaro = {
    'Pet:': 'Passáro',
    'Raça:': 'Periquito-australiano',
    'Dono:': 'Francisca Pereira',
}

pets = [cachorro, gato, passaro,]

for pet in pets:
    print(
        f'Dono(a): {pet['Dono:']}\n'
        f'Pet: {pet['Pet:']}' f'\tRaça: {pet['Raça:']}\n'
    )

favorite_places