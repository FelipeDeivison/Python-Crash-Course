names = ['Nathan', 'Guilherme', 'Roger', 'Rodrigo', 'Renan', 'Roberta']
print(names[0:6])

#Maneira mais fácil do exercicio do livro seria usando o 'for' para
#  criar um loop

for name in names:
    print(f'{name} disse "Oi"')

#O jeito que daria certo sem ser com o loop seria criar uma variavel
# para cada nome na lista:

mensagem = f'{names[0]} disse "Oi"'
mensagem1 = f'{names[1]} disse "Oi"'
print(mensagem)
print(mensagem1)

#3 pratica do livro

veiculos = ['Moto', 'Carro', 'Bicicleta', 'Skate']

veiculo1 = f'Andei de {veiculos[0]} hoje!'
veiculo2 = f'Fui de {veiculos[1]} para o treino'
veiculo3 = f'Brinquei com meu {veiculos[2]} ontem'
print(veiculo1)
print(veiculo2)
print(veiculo3)