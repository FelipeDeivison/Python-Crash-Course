games = ['TLOU', 'Uncharted', 'Tomb Raider', 'Clair Obscur', 'Skarking Zero', 'Astro Bot']
print("Os três primeiros elementos da lista são:")
print(games[0:3])

print("Os três primeiros elementos da lista são:")
for game in games[0:3]:
    print(game)

print("Os elementos do meio da lista são:")
for game in games[2:4]:
    print(game)

print('Os três ultimos elementos da lista são:')
for game in games[-3:]:
    print(game)

my_pizzas = ['Frango com Catupiry', 'Calabresa', 'Carne Seca']
friend_pizzas = ['Frango com Catupiry', 'Calabresa', 'Carne Seca']
friend_pizzas.append('Portuguesa')
my_pizzas.append("Quatro Queijos")

print('\nMinha pizzas favoritas são:\n')
for pizza in my_pizzas:
    print(pizza)

print('\nAs pizzas favoritas do meu amigo são:\n')
for pizza in friend_pizzas:
    print(pizza)
print()
foods = ['pizza', 'falafel', 'carrot coke', 'cannoli', 'ice cream']
for food in foods:
    print(food.title())