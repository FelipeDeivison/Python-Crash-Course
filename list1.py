convidados = ['Nathan', 'Roger', 'Guilherme']
for convidado in convidados:
    print(f'Felipe convidou {convidado} para a festa!\n')

print(f'{convidados[2]} não poderá ir para a festa.\n')

del convidados[2]
print(convidados)

convidados.append('Renan')
convidados.append('Roberta')
print(convidados)

for convidado in convidados[-2:]:
    print(f'Felipe convidou {convidado} para a festa!\n')

print('Caros convidados, encontrei um lugar maior para a festa, irei convidar mais alguns amigos.')

convidados.insert(0, 'Gustavo')
convidados.insert(3, 'Jonatan')
convidados.append('Ana')
print(convidados)

for convidado in convidados:
    print(f'Olá, {convidado}! Estou passando para informar o novo local para festa! ...')

print("Peço desculpas, infelizmente só poderei levar os pessoas")

amigo = convidados.pop()
print(f'Olá {amigo}! Por causa de um emprevisto não terei que cancelar a festa.\n')

amigo = convidados.pop()
print(f'Olá {amigo}! Por causa de um emprevisto não terei que cancelar a festa.\n')

amigo = convidados.pop()
print(f'Olá {amigo}! Por causa de um emprevisto não terei que cancelar a festa.\n')

amigo = convidados.pop()
print(f'Olá {amigo}! Por causa de um emprevisto não terei que cancelar a festa.\n')

amigo = convidados.pop()
print(f'Olá {amigo}! Por causa de um emprevisto não terei que cancelar a festa.\n')

print(convidados)

for convidado in convidados:
    print(f'Oi {convidado}, a festa foi cancelada mas vamos sair para jantar comigo e com meu amigo?\n')

del convidados[0]
del convidados[0]

print(convidados)
