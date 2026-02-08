# Alguns exemplos aleatorios de testes condicionais

carro = 'vermelho'
print(carro == 'vermelho')

carro = 'Vermelho'
print(carro == 'vermelho')

carro = 'Vermelho'
print(carro.lower() == 'vermelho')

celular = 'preto'
print(celular == 'PRETO')

celular = 'preto'
print(celular.upper() == 'PRETO')

academia = 'ABERTA'
print(academia == 'aberta')

academia = 'ABERTA'
print(academia == 'aberta'.upper())


carro = 'Azul'
if carro == 'Azul':
    print(f'O carro é {carro}!')

celular = 'ligado'
if celular == 'Descarregado':
    print('O celular precisa de carga!')
else:
    print("O celular ainde está com carga!")

videogame = 'Ligado'
if videogame.lower() == "ligado":
    print('Irei jogar um pouco')
else:
    print('Deixarei para jogar mais tarde.')

valor = 3
print(valor == 2) #False
print(valor >= 2) #True
print(valor <= 2) #False
print(valor != 2) #True

valor2 = 2
print((valor >= 2) and (valor2 <= 3)) #A primeira condição é True e a segunda é
#True também, logo a condição resulta em True.
print((valor == 3) or (valor2 ==3)) #A primeira condição é True e a segunda é 
#False, logo a condição é True, pois a palavra reservada é o "or".
print((valor == 5) or (valor2 == 6)) #false, pois os dois valores são false e 
#estamos usando "or"
print((valor == 4) and (valor2 == 2)) #false, um valor é True e o outro é false

names = ['Nathan', 'Guilherme', 'Roger', 'Rodrigo', 'Renan', 'Roberta']
print('roger' in names)
print('roger' in [name.lower() for name in names]) # IMPORTANTE!! 
#Tentei usar o "lower" com a lista igual as outros exemplos e não deu certo, o 
# jeito de usar é igual a maneira a cima

cores = ["Azul", "vermelho", "Amarelo", "verde"]
print('Vermelho' in [cor.title() for cor in cores])

nomes = ["ana", "Carlos", "joão", "maria"]
print('JOÃO' in [nome.upper() for nome in nomes])

#uso do 'any'
frases = [
    "Eu gosto de programar em Python", 
    "Hoje o dia está lindo", 
    "Python é poderoso"
  ]
tem_python = any('python' in frase.lower() for frase in frases)
print(tem_python)