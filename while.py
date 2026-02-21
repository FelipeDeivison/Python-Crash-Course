prompt = (
    'Quais ingredientes você quer em sua pizza? \n'
    'Para finalizar basta digitar "quit"\n'
          )
ingredientes = []
while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    ingredientes.append(pizza)

print(f'Os ingredientes que vai em sua pizza são: {ingredientes}')
    