from random import choice

class Loterica:
    def __init__(self):
        pass
    
    def numero_sortido(self):
        loteria = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
        cod = (
            f'{choice(loteria)}{choice(loteria)}'
            f'{choice(loteria)}{choice(loteria)}'
        )
        return cod

my_ticket = 6,"B",2,6
codigo_sorteado = Loterica()


tentativas = 0

while True:
    sortido = codigo_sorteado.numero_sortido()

    if sortido == my_ticket:
        print(f'Seu ticket {my_ticket} foi sorteado!')
    else:
        print(codigo_sorteado)

