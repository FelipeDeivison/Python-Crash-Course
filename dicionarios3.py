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

favorite_places = {
    'Viagem1': 'Japão',
    'Viagem2': 'Colombia',
    'Viagem3': 'New York',
}

print()

for lugar in favorite_places.values():
    if lugar == 'Japão':
        print(f'Felipe quer viajar futuramente para o {lugar}!\n')
    elif lugar == 'Colombia':
        print(f'João e Felipe iram viajar para a {lugar}!\n')
    else:
        print(f'Felipe e seus amigos estão planejando viajar para {lugar}!\n')

print()

favorites_numbers = {
    'natiara': [20, 38, 27],
    'felipe': [8, 6, 26, 18],
    'nathan': [16, 24, 32],
    'roberta': [18],
    'francisca': [21,35],
    }

for pessoa, numeros in favorites_numbers.items():
    print(f'{pessoa}: {numeros}')

print()

cities = {
    'São Paulo': {
        'coutry': 'Brasil',
        'population': '11,45 milhões',
        'fact': 'É a cidade mais populosa do hemisfério sul e o maior centro'
         ' financeiro da América Latina.',
    },
    
    'Fortaleza': {
        'coutry': 'Brasil',
        'population': '2,43 milhões',
        'fact': 'É uma das cidades mais ensolaradas do Brasil e tem uma das'
         ' maiores densidades populacionais do país.',
    },
    
    'Rio de Janeiro': {
        'coutry': 'Brasil',
        'population': '6,73 milhões',
        'fact': 'É famosa mundialmente pelo Rock in Rio e pelo Cristo Redentor,'
        ' uma das sete maravilhas do mundo moderno.',
    },
    }

for cidade, infos in cities.items():
    print(
        f'{cidade}\n\nPaís: {infos['coutry']}' 
        f'\tPopulação: {infos['population']}\n'
        f'\nInformações: {infos['fact']}\n'
        )