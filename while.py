# prompt = (
#     'Quais ingredientes você quer em sua pizza? \n'
#     'Para finalizar basta digitar "quit"\n'
#           )
# ingredientes = []
# while True:
#     pizza = input(prompt)
#     if pizza == 'quit':
#         break
#     ingredientes.append(pizza)

# print(f'Os ingredientes que vai em sua pizza são: {ingredientes}')

prompt1 = (
    'Bem vindos ao Cinama!\n'
    'Por gentileza, me informe sua idade: '
)

while True:
    idade = int(input(prompt1))
    if idade < 3:
        print('Ingresso Gratuito')
    elif idade <= 12:
        print("O ingresso custa U$10")
    else:
        print('O ingresso custa U$15')


    