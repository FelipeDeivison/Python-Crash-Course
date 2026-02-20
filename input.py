#Exercicio 1

carro = input('Qual o modelo do veiculo deseja alugar? ')
print(f'Vejamos se consigo encontrar o modelo {carro} para você!\n')

#Exercicio 2

print(
    'Boa noite!'
    '\nSejam Bem vindo ao Restaurante.'
    )
reserva = int(input('Quantos lugares deseja reservar? '))
if reserva > 8:
    print(
        'No momento não temos uma mesa disponivel\n'
        'Vocês podem esperar que logo mais estará disponivel.'
        )
else:
    print('Temos uma mesa á disposiçâo.')

#Exercicio 3
number = int(input('Digite um número: '))

if number % 10 == 0:
    print(f'O número "{number}" é miltiplo de 10!')
else:
    print(f'O númoro "{number}" não é multiplo de 10.')
