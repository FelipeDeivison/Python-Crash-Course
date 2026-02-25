# sandwich_orders = [
#     "X-Burger",
#     "X-Salada",
#     "X-Bacon",
#     "X-Tudo",
#     "Misto Quente",
#     "Hambúrguer Clássico",
#     "Cheeseburger",
#     "Frango Grelhado",
#     "Frango com Catupiry",
#     'Pastrami',
#     "Atum",
#     "Peito de Peru",
#     "Mortadela",
#     "Rosbife",
#     "Vegetariano",
#     'Pastrami',
#     "Vegano",
#     "BLT",
#     "Carne Louca",
#     "Pernil",
#     "Costela Desfiada",
#     "Filé com Queijo",
#     'Pastrami',
# ]

# print('Infelizmente não iremos ter Sanduíche de pastrami!')

# while 'Pastrami' in sandwich_orders:
#     sandwich_orders.remove('Pastrami')
    
# finished_sandwiches = []

# for sanduiche in sandwich_orders:
#     print(f'Seu sanduíche de {sanduiche} está pronto!')

# while sandwich_orders:
#     sanduiche = sandwich_orders.pop(0)
#     finished_sandwiches.append(sanduiche)
#     print(f'Opedido {sanduiche} foi finalizado!')

# finalizados = 0

# for sanduiche in finished_sandwiches:
#     finalizados += 1
#     print(f'O pedido n°{finalizados} - {sanduiche}')



prompt = (
    'Pesquisa Viagem dos sonhos\n'
    'Caso deseje sair basta digita "quit" na primeira pergunta\n'
    'Primeiro me diga como se chama: '
    )
viagens = []

while True:
    nome = input(prompt)
    if nome == 'quit':
        break

    lugar = input('Se você pudesse viajar para um lugar, qual seria? ')
    
    viagem = {'nome': nome, 'lugar': lugar}
    viagens.append(viagem)

for v in viagens:
    print(f'A viagem do sonhos de {v['nome']} é para {v['lugar']}')